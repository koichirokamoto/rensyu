package lib

import "github.com/gin-gonic/gin"

func Hello(w gin.ResponseWriter) {
	w.WriteHeader(200)
	w.Write([]byte("Hello, World"))
}
