# Bibliotecas de treinamento do modelo
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import Adam

from data_preprocessing import preprocess_train_data

def train_bot_model(train_x, train_y):
    

    # Compile o modelo
    

    # Ajuste e salve o modelo
    


# Chamando os métodos para treinar o modelo
train_x, train_y = preprocess_train_data()

train_bot_model(train_x, train_y)

