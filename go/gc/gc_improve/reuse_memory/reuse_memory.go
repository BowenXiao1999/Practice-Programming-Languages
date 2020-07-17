package main

import (
    "fmt"
    "net/http"
    _ "net/http/pprof"
)

func newBuf() []byte {
    return make([]byte, 10<<20)
}

/*
Run this server in local.
Use ab test to simulate high cocurrency reqeust.
You will find that the GC is frequent.
Try to solve it by create Sync.Pool.
*/

func main() {
    go func() {
        http.ListenAndServe("localhost:6060", nil)
    }()
	
	// when there is a request on /example2, it will new a buffer
	// when there are too many request, we should try to reuse them
    http.HandleFunc("/example2", func(w http.ResponseWriter, r *http.Request) {
        b := newBuf()

        // 模拟执行一些工作
        for idx := range b {
            b[idx] = 1
        }

        fmt.Fprintf(w, "done, %v", r.URL.Path[1:])
    })
    http.ListenAndServe(":8080", nil)
}