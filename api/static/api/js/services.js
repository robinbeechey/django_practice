'use strict';

/* Services */

var pollsServices = angular.module('pollsServices', ['ngResource']);

pollsServices.factory('Poll', ['$resource',
  function($resource){
    return $resource('questions/:id.json', {}, {
      query: {method:'GET', params:{id:'id'}, isArray:true}
    });
}]);
