model.fit(
    training_set,
    steps_per_epoch=100,
    epochs=10,
    validation_data=test_set,
    validation_steps=50
)