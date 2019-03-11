package main

import (
	_ "crypto/tls"
	"io/ioutil"
	"log"
	"net/http"
)

type CTAERROR struct {
	Code    int64  `"json:error.code"`
	Type    string `"json:error.type"`
	Message string `"json:error.message"`
}

func main() {

	http.HandleFunc("/vs/1.0/import-property-detail/", func(w http.ResponseWriter, req *http.Request) {
		data, err := ioutil.ReadFile("propertyDetails.json")
		if err != nil {
			log.Println("there are err when parse")
			panic(err)
		}
		log.Println(req.URL)
		w.WriteHeader(http.StatusOK)
		w.Write(data)
	})

	http.HandleFunc("/vs/1.0/enquire/", func(w http.ResponseWriter, req *http.Request) {
		data, _ := ioutil.ReadFile("cta_err.json")
		w.WriteHeader(http.StatusForbidden)
		w.Write(data)
	})

	// One can use generate_cert.go in crypto/tls to generate cert.pem and key.pem.
	log.Printf("About to listen on /vs/1.0/enquire/. Go to https://127.0.0.1:8443/")
	err := http.ListenAndServeTLS(":8443", "cert.pem", "key.pem", nil)
	log.Fatal(err)

	// http.HandleFunc("/vs/1.0/enquire/", func(w http.ResponseWriter, rq *http.Request) {
	// 	log.Println(rq.URL)
	// 	w.WriteHeader(http.StatusForbidden)
	// 	w.Write(data)
	// })
}
