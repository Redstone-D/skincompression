# Version 1 

## /v1/index GET 

**Pass in:** void 

**Return:** HTML index page 

## /v1/index POST 

**Pass in:** void 

**Pass in within a form:** 
* File Field multiple: files -> List of files the user input to pack 
* Text field: name -> Name of the skinpack 
* Text field: model -> Model of the skinpack, while N = Normal, G = Girl 

**Return:** File response 

# Version 2.1 

## v2/index GET (Abandon) 

**Pass in:** void 

**Return:** The default index page 

## v2/index POST 

Create a project with an initial input 

**Pass in:** void 

**Pass in within a form:** 
* File Field multiple: files -> List of files the user input to pack 
* Text field: name -> Name of the skinpack 

**Return:** v2/process/<rid: num> 
| Data | Explaination | 
| --- | --- | 
| rid: num | The rid the project | 

## v2/add/<rid: num> GET (Abandon) 

Add a skin into a project with a specified rid 

**Pass in:** void 

**Return:** Add page 

## v2/add/<rid: num> POST 

Add a skin into a project with a specified rid 

**Pass in:** void 

**Pass in within a form:** 
* File Field multiple: files -> List of files the user input to pack 

**Return:** JSON 
| Data | Explaination | 
| --- | --- | 
| rid: num | The rid the project | 
| pid: num | The pid the added skin | 

## v2/process/<rid: num> 

**Pass in:** id of request 

**Return:** json 
| Data | Explaination | 
| --- | --- | 
| rid: num | The rid the project | 

## v2/app/<rid: num> 

Get the JSON props of a Project (Request) 

**Pass in:** id of request 

**Return:** JSON 

| Data | Explaination | 
| --- | --- | 
| skin.id: num | The pid the specified skin | 
| skin.name: string | The name of the specified skin | 
| id: number | The request number |  

`
{ 
    "skins":[{
        "id": pid: num, 
        "name": name: string 
    } 
    (Other skins goes on) 
    ] 
    "id": int: rid 
} 
` 

## v2/changeName/<pid: num> POST 

Change a name of the skin 

**Pass in:** pid -> number indicates the id of the skin 

**Pass in within a form:** 
* Text Field: name -> new name of the skin 

**Return:** Json 
| Data | Explaination | 
| --- | --- | 
| status: num | 0 | 

## v2/changeModel/<pid: num> POST 

Change a model of the skin 

**Pass in:** pid -> number indicates the id of the skin 

**Pass in within a form:** 
* Text Field: model -> new model of the skin 

**Return:** Json 
| Data | Explaination | 
| --- | --- | 
| status: num | 0 | 

## v2/getskinprop/<pid: num> 

Get the proporties of a skin 

**Pass in:** pid -> number indicates the id of the skin 

**Return:** JSON 

| Data | Explaination | 
| --- | --- | 
| id: num | The pid of the skin | 
| name: string | The name of the skin | 
| model: string | The model of the skin |  

## v2/pircture/<pid: num> 

Get the picture of the skin 

**Pass in:** pid -> number indicates the id of the skin 

**Return:** File 

## v2/getcompress/<rid: num> 

Get the compressed skinpack 

**Pass in:** rid -> number indicates the id of the skin 

**Return:** File 

## v2/deleteskin/<pid: num> 

Delete a skin 

**Pass in:** pid -> the skin id 

**Return:** 1 
