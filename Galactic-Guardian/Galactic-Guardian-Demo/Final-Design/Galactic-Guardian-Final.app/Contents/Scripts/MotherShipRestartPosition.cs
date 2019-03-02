using System.Collections;
using System.Collections.Generic;
using UnityEngine;
// START...Mother-Ship-Restart-Position 
// GOAL: MotherShip restarts movement from original position in sandbox.
// After colliding with Restart1 trigger
public class MotherShipRestartPosition : MonoBehaviour {
    // Variables for Mother-Ship-Restart-Position 
    public Rigidbody enemy;
    Vector3 initialPos;
    // if object collides with trigger, game restart
    void OnTriggerEnter(Collider other) {
        if (other.CompareTag("Restart1")) {
            enemy.transform.position = initialPos;
            Update();
        }
    }
    // Update is called once per frame
    void Update() {
      // Updates console log of curent game status 
      Debug.Log("MOTHER SHIP RESTARTS POSITION");
    }
}
// END Mother-Ship-Restart-Position ...