package main

import (
	"io"
	"io/ioutil"
	"log"
	"os"
)

var (
	Trace  *log.Logger
	Infor  *log.Logger
	Waring *log.Logger
	Error  *log.Logger
)

func init() {
	file, err := os.OpenFile("errors.txt",
		os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
	if err != nil {
		log.Fatalln("Failed to open error log file: ", err)
	}

	Trace = log.New(ioutil.Discard,
		"TRACE: ",
		log.Ldate|log.Ltime|log.Lshortfile)

	Infor = log.New(os.Stdout,
		"INFO: ",
		log.Ldate|log.Ltime|log.Lshortfile)

	Waring = log.New(os.Stdout,
		"WARNING: ", log.Ldate|log.Ltime|log.Lshortfile)

	Error = log.New(io.MultiWriter(file, os.Stderr),
		"ERROR: ", log.Ldate|log.Ltime|log.Lshortfile)
}

// func main() {
// 	Trace.Println("I have something standard to say")
// 	Infor.Println("Special information")
// 	Waring.Println("There is something you need to know about")
// 	Error.Println("Something has failed")
// }
