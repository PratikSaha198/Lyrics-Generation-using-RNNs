# Lyrics-Generation-using-RNNs
## This project generates new lyrics which did'nt exist before using Recurrent-Neural-Networks (RNNs) from a data-set created by web scrapping [The GENIUS website](https://genius.com/) using its API.  

## _**After vectorizing the text and creating training examples and targets , a four layer model was used. The Four layers used are :**_
####  **1. Embedding layer :** The input layer. A trainable lookup table that will map the numbers of each character to a vector with embedding_dim dimensions
####  **2. GRU layer :** A type of RNN with size units=rnn_units (Birectional-LSTM could also be used here.)
#### **3. Dense layer :** The output layer, with vocab_size outputs and 'RELU' as the activation fuction 
#### **4. Dropout layer :** Benifits regularisation and prevents overfitting  

## _**The final prediction loop for text generation works as follows**_
![Image of something](https://www.tensorflow.org/tutorials/text/images/text_generation_sampling.png)

## _**Steps to implement this project :**_
#### 1. Fork the repository.
#### 2. Put [lyrics_scrapper_from_GENIUS_website.py](lyrics_scrapper_from_GENIUS_website.py) and [lyrics_dataset_creator.py](lyrics_dataset_creator.py) in the same directory.
#### 3. Execute [lyrics_scrapper_from_GENIUS_website.py](lyrics_scrapper_from_GENIUS_website.py) to fetch the songs of a particular from [The GENIUS website](https://genius.com/) in a JSON file. (number of songs , title , popularity and be mentioned).
#### 4. Execute [lyrics_dataset_creator.py](lyrics_dataset_creator.py) to parse the JSON files , selecting just the 'lyrics' key. It also creates the dataset named 'lyrics_dataset.txt' after doing some data-cleansing.
#### 5. Run the [Lyrics_Generation.ipynb](Lyrics_Generation.ipynb) notebook (preferably in Google Collab with GPU support for faster execution) , uploading the 'lyrics_dataset.txt' file , getting the new lyrics being generated. 
#### 6. Tweak the hyper-parameters according to "YOUR" best results

### My dataset used to train and get the output is ->  [lyrics_dataset.txt](lyrics_dataset.txt)

## _**Some lyrics generated :**_
#####    ```Love in the world``` 
#####    ```Happens each time to keep me warm```
#####    ```Love in the rain```
#####    ```And we'll stop eating food and I'll say the words that I want in this cold```
#####    ```I don't have to think that I want to do```
#####    ```I can't think of anyone, anyone else```
#####    ```And we gotta save ourselves```
#####    ```If we want it to be```
#####    ```I'll be taking my time```
#####    ```As she looks lovely in the wood```

## _**Scope for improvements :**_
#### 1. Using a LSTM-GAN based model, it has the best potential for most coherent output.
#### 2. Adding another layer of Birectional-LSTM and lowering the EPOCHS keeping the loss within 1.5 to 1.1 , for most meaningful text generated.
