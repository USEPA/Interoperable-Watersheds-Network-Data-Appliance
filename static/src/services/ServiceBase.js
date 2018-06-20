class ServiceBase {

    constructor(apiPath){
        this.api = apiPath
        this.get = this.get
        this.post = this.post
        this.put = this.put
        this.delete = this.delete
        this.API_GATEWAY = process.env.REACT_APP_API_GATEWAY ? process.env.REACT_APP_API_GATEWAY  : 'localhost'
        this.urlBase = 'http://'+this.API_GATEWAY+':5000/'+this.api
    }

    get(key){
        let url = key ? this.urlBase+key : this.urlBase
        return fetch(url, {
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, same-origin, *omit
            headers: {'content-type': 'application/json'},
            method: 'GET', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, cors, *same-origin
            redirect: 'follow', // manual, *follow, error
            referrer: 'no-referrer', // *client, no-referrer
        })
    }
    
    post(payload){
        let url = this.urlBase
        return fetch(url,{
            body: JSON.stringify(payload),
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, same-origin, *omit
            headers: {'content-type': 'application/json'},
            method: 'POST', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, cors, *same-origin
            redirect: 'follow', // manual, *follow, error
            referrer: 'no-referrer', // *client, no-referrer
        })
        .then( response => response.json())
    }

    put(key, payload){
        let url = this.urlBase+'/'+key
        return fetch(url,{
            body: JSON.stringify(payload),
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, same-origin, *omit
            headers: {'content-type': 'application/json'},
            method: 'PUT', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, cors, *same-origin
            redirect: 'follow', // manual, *follow, error
            referrer: 'no-referrer', // *client, no-referrer
        })
        .then( response => response.json())
    }

    delete(key){
        let url = this.urlBase+'/'+key
        return fetch(url,{
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, same-origin, *omit
            headers: {'content-type': 'application/json'},
            method: 'DELETE', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, cors, *same-origin
            redirect: 'follow', // manual, *follow, error
            referrer: 'no-referrer', // *client, no-referrer
        })
        .then( response => response.json())
    }
}
