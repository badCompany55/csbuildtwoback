
# CS Build Week Two Backend
## Django

## Endpoints
### All endpoints require the JWT token in the header
* Authorization -> -> Bearer token
### Endpoints that access the Lambda api, the provided api key is required in the header as well
* backKey -> -> api key

1. api/token
    * Request Type = Post 
    * Provide {"username": "username", "password": "password"} in the body, RESPONSE = JWT Token, Labmda api key per user, and user id.
        
2. api/loot
    * Request Type = Get
    * Implements phil's search algo, searches the map until 1000 treasure is aquired. Returns back to start
    
3. api/piraterys
    * Request Type = Get
    * Implements phil's travel to algo, travels to the pirateys location.
    * Name change location.
    
4. api/brightlylitroom
    * Request Type = Get
    * Implements phil's travel to algo, travels to the brightly lit room location.

5. api/shop
    * Request Type = Get
    * Implements phil's travel to algo, travels to the shop location.
    
6. api/mistyroom
    * Request Type = Get
    * Implements phil's travel to algo, travels to the misty room location.
    
7. api/mtholloway
    * Request Type = Get
    * Implements phil's travel to algo, travels to the mt holloway location.
    
8. api/peakmtholloway 
    * Request Type = Get
    * Implements phil's travel to algo, travels to the peak mt holloway location.
    
9. api/transmogriphier
    * Request Type = Get
    * Implements phil's travel to algo, travels to the transmogriphier location.
    
10. api/adarkcave
    * Request Type = Get
    * Implements phil's travel to algo, travels to the a dark cave location.
    
11. api/linhsshrine
    * Request Type = Get
    * Implements phil's travel to algo, travels to the a linhs shrine location.
    
12. api/glassowynsgrave
    * Request Type = Get
    * Implements phil's travel to algo, travels to the a glassowyns grave location.
    
13. api/wishingwell
    * Request Type = Get
    * Implements phil's travel to algo, travels to the a wishing well location.

14. api/map
		* Request Type = Get
		* Map endpoint

