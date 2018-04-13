package appengine

import (
	"github.com/gin-gonic/gin"

	"github.com/koichirokamoto/tryit/appengine/lib"
)

func init() {
	engine := gin.New()
	engine.Any("/hello", func(c *gin.Context) {
		lib.Hello(c.Writer)
	})
}
