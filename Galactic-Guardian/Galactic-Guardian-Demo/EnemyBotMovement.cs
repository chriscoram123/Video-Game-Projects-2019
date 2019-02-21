using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyBotMovement : MonoBehaviour {
    public Rigidbody En;
    public float speed;
    // Start is called before the first frame update
    void Start() {
        
    }

    // Update is called once per frame
    void Update() {
        En.AddForce(0,0, speed * Time.deltaTime);
        Debug.Log("ENEMY BOT IS MOVING"); 
    }
}
