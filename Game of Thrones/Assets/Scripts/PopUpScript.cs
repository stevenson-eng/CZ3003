using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;

public class PopUpScript : MonoBehaviour
{

    public Button closeButton;
    public Text errorMessage;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void Init(Canvas canvas, string errorMessage)
    {
        Debug.Log(this.gameObject.transform.localPosition);

        transform.SetParent(canvas.transform);
        transform.position = new Vector3(1000, 1000, 0);


        this.errorMessage.text = errorMessage;
        closeButton.onClick.AddListener(() =>
        {
            GameObject.Destroy(this.gameObject);
        });
    }
}
