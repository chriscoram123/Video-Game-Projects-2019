using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyBotDestroy : MonoBehaviour {
    public Rigidbody EnemyBots;
    public Transform EnemyStart;
    void OnTriggerEnter(Collider other) {
        if (other.CompareTag("Bullet")) {
            Destroy(gameObject, 0.1f);
            Instantiate(EnemyBots, EnemyStart.position, EnemyStart.rotation);
            Update();
        }
    }

    // Update is called once per frame
    void Update() {
        Debug.Log("ENEMY OBJECT WILL DISSAPEAR THEN RE-APPEAR");
    }
}
