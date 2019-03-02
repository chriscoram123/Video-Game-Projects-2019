using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class InstantiatePlasmaRay : MonoBehaviour {
    public Rigidbody Projectiles;
    public Transform barrelEnd;
    public float speed;
    // Update is called once per frame
    void Update() {
        if(Input.GetKey("e")) {
            Instantiate(Projectiles, barrelEnd.position, barrelEnd.rotation);
            Projectiles.AddForce(500 * speed * Time.deltaTime, 0, 0);
        }
    }
}
