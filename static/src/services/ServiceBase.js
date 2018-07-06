export default class ServiceBase {

    constructor(apiPath){
        this.api = apiPath;
        this.get = this.get;
        this.post = this.post;
        this.put = this.put;
        this.delete = this.delete;
        this.API_GATEWAY = process.env.REACT_APP_API_GATEWAY ? process.env.REACT_APP_API_GATEWAY  : 'localhost';
        this.API_PORT = process.env.REACT_APP_API_PORT ? process.env.REACT_APP_API_PORT  : '5000';
        this.urlBase = 'http://'+this.API_GATEWAY+':'+this.API_PORT+'/'+this.api;
    }

    get(key, callback){
        let url = key ? this.urlBase+key : this.urlBase;
        return fetch(url, {
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, same-origin, *omit
            headers: {'content-type': 'application/json'},
            method: 'GET', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, cors, *same-origin
            redirect: 'follow', // manual, *follow, error
            referrer: 'no-referrer', // *client, no-referrer
        }).then(response => {
            return response.json();
        }).then(function(json) {
            callback(json);
        }).catch((error) => {
            console.log(error);
        });
    }
    
    post(payload, callback){
        let url = this.urlBase;
        return fetch(url,{
            body: JSON.stringify(payload),
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, same-origin, *omit
            headers: {'content-type': 'application/json'},
            method: 'POST', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, cors, *same-origin
            redirect: 'follow', // manual, *follow, error
            referrer: 'no-referrer', // *client, no-referrer
        }).then(response => {
            return response.json();
        }).then(function(json) {
            callback(json);
        }).catch((error) => {
            console.log(error);
        });
    }

    put(key, payload, callback){
        let url = this.urlBase+'/'+key;
        return fetch(url,{
            body: JSON.stringify(payload),
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, same-origin, *omit
            headers: {'content-type': 'application/json'},
            method: 'PUT', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, cors, *same-origin
            redirect: 'follow', // manual, *follow, error
            referrer: 'no-referrer', // *client, no-referrer
        }).then(response => {
            return response.json();
        }).then(function(json) {
            callback(json);
        }).catch((error) => {
            console.log(error);
        });
    }

    delete(key, callback){
        let url = this.urlBase+'/'+key;
        return fetch(url,{
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, same-origin, *omit
            headers: {'content-type': 'application/json'},
            method: 'DELETE', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, cors, *same-origin
            redirect: 'follow', // manual, *follow, error
            referrer: 'no-referrer', // *client, no-referrer
        }).then(response => {
            return response.json();
        }).then(function(json) {
            callback(json);
        }).catch((error) => {
            console.log(error);
        });
    }
}
