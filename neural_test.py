from keras.models import Sequential
from keras.layers import Dense

model = Sequential([
    Dense(32, activation = 'relu', input_shape = (10,)),
    Dense(32, activation = 'relu'),
    Dense(1, activation = "sigmoid'),
])

    
model.compile(optimizer="sgd',
              loss='binary_crossentropy',
              metrics=['accuracy'])

hist = model.fit(X_train, Y_train,
                 batch_size=32, epochs=100,
                 validation_data=(X_val, Y_val)))
model.evaluate(X_test, Y_test)[1]
    
