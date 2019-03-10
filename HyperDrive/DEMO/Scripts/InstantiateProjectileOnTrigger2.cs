using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyBulletInstantiate : MonoBehaviour {
    public Rigidbody Bullet;
    public float speed;
    public float speed2;
    public float destroyTime;
    public Rigidbody barrelEnd;

    void OnTriggerEnter(Collider other) {
        if(other.CompareTag("Controller")) {
            Instantiate(Bullet, barrelEnd.position, barrelEnd.rotation);
            Bullet.AddForce(speed * Time.deltaTime, speed2 * Time.deltaTime, 0);
            Destroy(Bullet, destroyTime);
            Update();
        }
    }

    // Update is called once per frame
    void Update() {
        Debug.Log("BULLET HAS BEEN LAUNCHED AND WILL BE DESTROYED WITHIN X AMOUNT OF SECONDS");
    }
}
