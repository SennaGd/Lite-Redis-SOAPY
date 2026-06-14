package main

import (
	"net"
	"fmt"
	"strconv"
)

const (
	STRING  = '+'
	ERROR   = '-'
	INTEGER = ':'
	BULK    = '$'
	ARRAY   = '*'
)

func handleConnection(conn net.Conn) {
	defer conn.Close()

	buffer := make([]byte, 1024)
	for {
		n, err := conn.Read(buffer) // return x amount of indices
		if err != nil {
			fmt.Println("error reading received buffer")	
			return
		}
		
		// parsing received input to string	
		var receivedStr string 
		var receivedType string
		var receivedLen string

		receivedType = string(buffer[9])

		for i := range n-9 {
			i += 9
			if string(buffer[i]) == `\`{ 
				fmt.Printf(`\ found`)	
				break
			}
			if _, err := strconv.Atoi(string(buffer[i])); err == nil{
				receivedLen += string(buffer[i])
			}
			fmt.Println(string(buffer[i]))
		}

		intLen, err := strconv.Atoi(receivedLen)
		if err != nil {
			fmt.Println("could not parse to int")
			return
		}
		fmt.Printf("\nType: %v, Lenght: %v\n", receivedType, intLen)
		// buffer[11]+[12] == \r\n	

		// read the message
		for i:=0; i<intLen; i++{
		//	fmt.Println(string(buffer[12+i]), i, buffer[12+i])
			receivedStr += string(buffer[15+i])
		}
		fmt.Println(receivedStr)
		conn.Write([]byte("+Message received\r\n"))
	}	
}

func main() {
	fmt.Println("Server running on port: 6379")
	server, err := net.Listen("tcp", ":6379")	
	if err != nil {
		return
	}
	for {
		conn, err := server.Accept()	
		if err != nil {
			continue	
		}
		go handleConnection(conn)
	}
}
