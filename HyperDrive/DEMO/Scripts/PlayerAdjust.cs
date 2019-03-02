// START...player-movemnts-2D = DEMO
// GOALS: To get player to move forward in 2D area

// Variables for player-movements
Public Rigidbody Player;
Public float speed; 

void Update() {
    // If statement declares change in position with Player 
    if(Input.GetKey(KeyCode.UpArrow)) {
     // Force is added to increase position on y-axis(Positive)
       Player.AddForce(0, speed * Time.deltaTime, 0);
         // Updates to console log
       Debug.Log("POSITIVE PLAYER MOVEMENT ACTIVATED");
}
    }
    if else(Input.GetKey(KeyCode.DownArrow)) {
     // Force is added to decrease position on y-axis(Negative)
       Player.AddForce(0, -speed * Time.deltaTime, 0);
         // Updates to console log
       Debug.Log("NEGATIVE PLAYER MOVEMENT ACTIVATED");
}
    }
     // Updates to console log
     Debug.Log("PLAYER MOVEMENT ACTIVATED");
}
// END...player-movemnts-2D = DEMO