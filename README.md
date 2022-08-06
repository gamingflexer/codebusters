# codebusters

## Ml Piplines

## OCR

### Request

`POST /api/ocr`

    file upload with key as 'file'

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 9999 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    {"data": {"ocrText": "Hello World in the image"}}

## translate

### Request

`POST /api/translate`

    {'text' : 'text to translate'}

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 9999 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    {"data": {"translatedText": "text to translate"}}


## detection

### Request

`POST /api/detection`

    file upload with key as 'file'

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 9999 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    {"data": {"detectionEntites": "Test out this"}}

## summarize

### Request

`POST /api/summarize`

    {'text' : 'text to summarize'}

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 9999 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    {"data": {"summarizedText": "text to summarize"}}

## NER

### Request

`POST /api/ner`

    {'text' : 'text to get entities'}

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 9999 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    {"data": {"entites": "dict with entities and lots of nan (so skip them)"}}