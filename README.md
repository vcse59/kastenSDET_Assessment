# kastenSDET_Assessment
Automated test cases to validate end points


Script Output:
==============

******************************************Scenario 1***********************************************
findPets: Received successful response
addPet: Received successful response
findPetByID: Received successful response
http://vivek.tj.dev.do.kasten.io/api/pets/23
deletePetByID: Received successful response
Record with id : 23 is succeessfully deleted
Scenarion Execution 1 is passed
****************************************************************************************************


******************************************Scenario 2***********************************************
findPets: Error code 404 message path /api/path was not found
Scenarion Execution 2 is passed
****************************************************************************************************


******************************************scenario 3***********************************************
http://vivek.tj.dev.do.kasten.io/api/path/3
deletePetByID: Error code 404 message path /api/path/3 was not found
Scenarion Execution 3 is passed
****************************************************************************************************


******************************************scenario 4***********************************************
addPet: Received successful response
findPetByID: Received successful response
Record is succeessfully found for 86
Scenarion Execution 4 is passed
****************************************************************************************************
