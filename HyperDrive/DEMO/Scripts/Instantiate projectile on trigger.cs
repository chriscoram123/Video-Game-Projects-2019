// START...Instantiate projectile on trigger = DEMO
// GOALS: If player moves into trigger zone, instantiate projectile

// Variables for Instantiate projectile on trigger
Public Rigidbody EnemyTurret;
Public Rigidbody Player;
Public Rigidbody PlasmaBeam;
Public float speed;

void OnTriggerEnter(Collider other) {
    // If statement declares that once an object interacts
    // with trigger, Plasma Beam object will instantiate and 
    // move forward.
   if(other.CompareTag("Player1")) {
     // Unity instantiates object from preFab
    Instantiate(PlasmaBeam);
     // Unity AddsForce
    PlasmaBeam.AddForce(0,0, speed * Time.deltaTime);
    update();
   }
}

void update {
    // Updates to console log
     Debug.Log("PLASMA BEAM HAS INSTANTIATED AND ACCELERATED");
}
// END...Instantiate projectile on trigger = DEMO