// START...player-movemnts-Forward-Force = DEMO
// GOALS: To get player to move forward in 2D area

// Variables for player-movements
Public Rigidbody Player;
Public float speed; 

void Update() { 
    // As soon as game starts, add force to object
     Player.AddForce(0, 0, speed * Time.deltaTime);
       // Updates to console log
         Debug.Log("PLAYER IS MOVING");
}
// END...player-movemnts-2D = DEMO