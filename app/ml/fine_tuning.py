from transformers import Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def fine_tune_model(model_name: str, dataset_path: str, output_dir: str, epochs: int = 3, batch_size: int = 4):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    dataset = load_dataset('text', data_files={'train': dataset_path})
    def tokenize_function(examples):
        return tokenizer(examples['text'], truncation=True, max_length=512)

    tokenized_dataset = dataset.map(tokenize_function, batched=True, remove_columns=["text"])

    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    training_args = TrainingArguments(
        output_dir=output_dir,
        overwrite_output_dir=True,
        num_train_epochs=epochs,
        per_device_train_batch_size=batch_size,
        save_steps=500,
        save_total_limit=2,
        logging_dir=f'{output_dir}/logs',
        logging_steps=100,
        evaluation_strategy="steps",
        eval_steps=500,
        report_to="none",
        weight_decay=0.01,
        learning_rate=5e-5,
        warmup_steps=200,
        fp16=torch.cuda.is_available(),
        push_to_hub=False,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset['train'],
        data_collator=data_collator,
    )

    trainer.train()
    trainer.save_model(output_dir)
