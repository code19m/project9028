package main

import (
	"log"
	"net"
	"net/http"

	_ "github.com/Nuriddin-Olimjon/project9028/frontEnd/statik"
	"github.com/rakyll/statik/fs"
)

func main() {
	mux := http.NewServeMux()

	statikFS, err := fs.New()
	if err != nil {
		log.Fatal("failed to create statik file service:", err)
	}

	mux.Handle("/", http.FileServer(statikFS))

	listener, err := net.Listen("tcp", "0.0.0.0:3000")
	if err != nil {
		log.Fatal("failed to create new listener:", err)
	}

	log.Print(`Starting statik service on address "0.0.0.0:3000"`)
	err = http.Serve(listener, mux)
	if err != nil {
		log.Fatal("failed to start serving:", err)
	}
}
