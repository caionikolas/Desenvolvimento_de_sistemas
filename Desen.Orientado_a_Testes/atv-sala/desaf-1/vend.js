function queue(){
    let itens = []

    this.enqueue = function(e){
        itens.push(e)
    }

    this.dequeue = function(){
        itens.shift()
    }

    this.front = function(){
        return itens[0]
    }

    this.isEmpty = function(){
        return itens.length === 0
    }

    this.size = function(){
        return itens.length
    }

    this.print = function(){
        console.log(itens.toString())
    }
}


let grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["alice"] = ["peggy"]
grafo["bob"] = ["anuj", "peggy"]
grafo["claire"] = ["thom","jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []

var fila = new queue()
fila.enqueue(grafo["voce"])
File.print()



