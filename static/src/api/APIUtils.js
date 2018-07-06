class APIUtils {
    static getPropertyValue(object, property) {
        return object.hasOwnProperty(property) ? object[property] : '';
    }
}