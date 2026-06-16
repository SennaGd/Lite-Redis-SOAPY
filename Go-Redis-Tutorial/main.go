package main

import (
	"fmt"
	"net"
)

func main() {
	//	input := "$5\r\nSenna\r\n"
	//	reader := bufio.NewReader(strings.NewReader(input))
	//
	//	b, _ := reader.ReadByte()
	//
	//	if b != '$' {
	//		fmt.Println("invalid type")
	//		os.Exit(1)
	//	}
	//
	//	size, _ := reader.ReadByte()
	//	strSize, _ := strconv.ParseInt(string(size), 10, 64)
	//
	//	reader.ReadByte()
	//	reader.ReadByte()
	//
	//	name := make([]byte, strSize) // Allocate strsize amount of bytes
	//	reader.Read(name)
	//
	//	fmt.Println(string(name))

	l, err := net.Listen("tcp", ":6379")

	if err != nil {
		fmt.Println(err)
		return
	}

	conn, err := l.Accept()

	if err != nil {
		fmt.Println(err)
		return
	}

	defer conn.Close() // delay connection close

	for {
		resp := NewResp(conn)
		value, err := resp.Read()
		if err != nil {
			fmt.Println(err)
			return
		}
		fmt.Println(value)
		conn.Write([]byte("+OK\r\n"))
	}
}
