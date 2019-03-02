using System.Collections;
using System.Collections.Generic;
using UnityEngine;
// START...enemy bot destroy
// GOAL: Enemy boys will be destroyed when triggered with Player Bullet
public class EnemyBotDestroy : MonoBehaviour {
    // Variables for enemy bot
    public Rigidbody enemyBot;

    // OntriggerEnter will destroy game object when on collision contact 
    // with an object containing the Player Bullet tag 
    void OntriggerEnter(Collider other) {
        if(other.CompareTag("PlayerBullet")) {
            // Destroy game object
            Destroy(enemyBot, 0.1f);
            Update();
        }
    }

    // Update is called once per frame
    void Update() {
        // Updates console log of curent game status 
        Debug.Log("ENEMY DESTROYED");
    }
}
// END ENEMY BOT DESTROYED...
