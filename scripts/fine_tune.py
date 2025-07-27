from app.ml.fine_tuning import fine_tune_model

if __name__ == "__main__":
    model_name = "mosaicml/mpt-7b-storywriter"
    dataset_path = "data/story_dataset.txt"  # Hikayelerin olduğu düz metin dosyası
    output_dir = "fine_tuned_model"
    epochs = 3
    batch_size = 2

    fine_tune_model(
        model_name=model_name,
        dataset_path=dataset_path,
        output_dir=output_dir,
        epochs=epochs,
        batch_size=batch_size,
    )
