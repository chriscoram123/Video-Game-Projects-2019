using System.Collections;
using System.Collections.Generic;
using UnityEngine;
// START...Mother-Ship-
// GOAL: Initiate motherShip movement from original position in sandbox.
public class MotherShipScript : MonoBehaviour {
    // Variables for Mother-Ship-
    public Rigidbody enemy;
    public float speed;
    Vector3 originalPos;

    // Update is called once per frame
    // Force will be added to object
    void Update() {
        enemy.AddForce(speed * Time.deltaTime, 0, 0);
        // Updates console log of curent game status 
        Debug.Log("MOTHER SHIP IS MOVING");
    }
}
// END Mother-Ship-...