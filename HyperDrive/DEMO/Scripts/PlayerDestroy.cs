// START...Destroy player on trigger = DEMO
// GOALS: If player moves into trigger zone, destroy

// Variables for Destroy player on trigger
Public Rigidbody Player;

void OnTriggerEnter(Collider other) {
    // If statement declares that once an object interacts
    // with trigger, Player will be destroyed.
   if(other.CompareTag("TurretProjectile")) {
     Destroy(Player, 0.2f);
      Update();
   }
}

void Update() {
  // SceneManager changes scene when player is destroyed
  Scene.Load("GameOver");
   // Updates to console log
   Debug.Log("GAME OVER");
 }
}
// END...Destroy player on trigger = DEMO