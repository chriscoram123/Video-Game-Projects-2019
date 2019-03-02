using System.Collections;
using System.Collections.Generic;
using UnityEngine;
// START...Cluster 2 movement
// GOALS: Provide cluster 2 two with force and direction during gamepley
public class Cluster2Movement : MonoBehaviour {
    // Variables for cluster 2 movement 
    public Rigidbody enemy;
    public float speed;
    Vector3 originalPos;

    // Update is called once per frame
    void Update() {
        // Force and direction will be attributed to game object
        enemy.AddForce(0, 0, speed * Time.deltaTime);
          // Updates console log of curent game status 
          Debug.Log("CLUSTER 2 HAS STARTED MOVEMENT");
    }
}
// END CLUSTER 2 MOVEMENT...