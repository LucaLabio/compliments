<div align=center><h1> Compliments </h1></div>
<h3 align=center>Simple API that uses sqlite to store and search for compliments on its local database</h3>
<h4>Requesting for a compliment</h4>

|property|description|
|---|---|
|**URL** | `/compliment/`|
|**Method** | `GET`|
|**Query** | `language - str`|
|**Query** | `compliment_number - str`|


**Request**: Search the database looking for any compliment matching the specified language, then generates random numbers based on compliment_number and returns these compliments

|field|description|
|---|---|
|**id** | `id number on database`|
|**text** | `The compliment`|
|**language** | `Language of the compliment`|

<h4>Inserting a new compliment</h4>

|property|description|
|---|---|
|**URL** | `/compliment/add/`|
|**Method** | `POST`|
|**Body** | `Json with text and language to be inserted on the database`|

**Request**: Register into the database a compliment

|field|description|
|---|---|
|**text** | `The compliment to be inserted`|
|**language** | `The language of the compliment to be inserted`|
