function validateEmail(email) { 
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}
function LoginController($scope, $element, $http, $timeout, $location)
{
	$scope.error_flag = false;
	$scope.init = function(csrf_token)
    {
        $scope.csrf_token = csrf_token;     
    }
	$scope.login_form_validation = function(){
	    if($scope.username == undefined || $scope.username == '') {
	        $scope.error_message = 'Please Enter your username';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.password == undefined || $scope.password == '') {
	        $scope.error_message = 'Please Enter Password';
	        $scope.error_flag = true;
	        return false;
	    }
	    return true;
	}
    $scope.login = function(){
    	$scope.is_valid = $scope.login_form_validation();
		if($scope.is_valid) {
		    params = {
		        'username': $scope.username,
		        'password': $scope.password,
		        "csrfmiddlewaretoken" : $scope.csrf_token
		    }
		    $http({
		        method : 'Post',
		        url : "/accounts/login/",
		        data : $.param(params),
		        headers : {
		        'Content-Type' : 'application/x-www-form-urlencoded'
		        }
		    }).success(function(data, status)
		    {

		        if(data.result == 'error'){
		        	alert('Hiii');
		            $scope.error_message = data.message;
		            $scope.error_flag = true;
		        } else {
		            $scope.username = '';
		            $scope.password = '';
		            document.location.href='/';
		        }             
		    }).error(function(data, status)
		    {
		        $scope.error_message = data.message;
		        $scope.error_flag = true;
		    }); 
		}
    }
}
function register_form_validation($scope) {
    if($scope.firstname == undefined || $scope.firstname == '') {
        $scope.error_message = 'Please Enter your First Name';
        $scope.error_flag = true;
        return false;
    } else if($scope.lastname == undefined || $scope.lastname == '') {
        $scope.error_message = 'Please Enter Last Name';
        $scope.error_flag = true;
        return false;
    } else if($scope.username == undefined || $scope.username == '') {
        $scope.error_message = 'Please Enter Username';
        $scope.error_flag = true;
        return false;
    } else if($scope.password == undefined || $scope.password == '') {
        $scope.error_message = 'Please Enter Password';
        $scope.error_flag = true;
        return false;
    } else if(!(validateEmail($scope.email)) ) {
        $scope.error_message = 'Please Enter Email Id';
        $scope.error_flag = true;
        return false;
    } else if($scope.user_type == undefined || $scope.user_type == '' || $scope.user_type == 'select') {
        $scope.error_message = 'Please Choose User Type';
        $scope.error_flag = true;
        return false;
    } else if($scope.user_type == 'vendors') {
    	if ($scope.brand == '' || $scope.brand == undefined) {
    		$scope.error_message = 'Please Enter Brand Name';
	        $scope.error_flag = true;
	        return false;
    	} 
    } 
    return true;
}
function SignupController($scope, $element, $http, $timeout, $location)
{
	$scope.error_flag = false;
	$scope.is_vendor = false;
	$scope.init = function(csrf_token)
    {
        $scope.csrf_token = csrf_token; 
        $scope.user_type = 'select';    
    }
    $scope.is_user_type_vendor = function(){
    	if ($scope.user_type == 'vendors') {
    		$scope.is_vendor = true;
    	} else {
    		$scope.is_vendor = false;
    	}
    }
    $scope.signup = function(){
    	$scope.is_valid = register_form_validation($scope);
    	if($scope.is_valid) {
		    params = {
		    	'firstname': $scope.firstname,
		    	'lastname': $scope.lastname,
		        'username': $scope.username,
		        'password': $scope.password,
		        'email': $scope.email,
		        'user_type':$scope.user_type,
		        'brand': $scope.brand,
		        "csrfmiddlewaretoken" : $scope.csrf_token
		    }
		    $http({
		        method : 'Post',
		        url : "/register/",
		        data : $.param(params),
		        headers : {
		        'Content-Type' : 'application/x-www-form-urlencoded'
		        }
		    }).success(function(data, status)
		    {

		        if(data.result == 'error'){
		            $scope.error_message = data.message;
		            $scope.error_flag = true;
		        } else {
		            $scope.username = '';
		            $scope.password = '';
		            $scope.firstname = '';
		    		$scope.lastname = '';
		        	$scope.email = '';
		        	$scope.user_type = '';
		        	$scope.brand = '';
		            document.location.href = '/accounts/login/';
		        }             
		    }).error(function(data, status)
		    {
		        $scope.error_message = data.message;
		        $scope.error_flag = true;
		    }); 
		}
    }
}

function AddSubDealerController($scope, $element, $http, $timeout, $location)
{
	$scope.error_flag = false;
	$scope.init = function(csrf_token, user_id)
    {
        $scope.csrf_token = csrf_token;  
        $scope.user_id = user_id;
        $scope.user_type = 'select';
    }
    $scope.add_subdealer = function (){
    	$scope.is_valid = register_form_validation($scope);
    	console.log($scope.is_valid);
    	if($scope.is_valid) {
		    params = {
		    	'firstname': $scope.firstname,
		    	'lastname': $scope.lastname,
		        'username': $scope.username,
		        'password': $scope.password,
		        'email': $scope.email,
		        'user_type':$scope.user_type,
		        "csrfmiddlewaretoken" : $scope.csrf_token
		    }
		    $http({
		        method : 'Post',
		        url : "/dealer/"+$scope.user_id+"/add/subdealer/",
		        data : $.param(params),
		        headers : {
		        'Content-Type' : 'application/x-www-form-urlencoded'
		        }
		    }).success(function(data, status)
		    {
		        if(data.result == 'error'){
		            $scope.error_message = data.message;
		            $scope.error_flag = true;
		        } else {
		            $scope.username = '';
		            $scope.password = '';
		            $scope.firstname = '';
		    		$scope.lastname = '';
		        	$scope.email = '';
		        	$scope.user_type = '';
		        	$scope.brand = '';
		            document.location.href = '/';
		        }             
		    }).error(function(data, status)
		    {
		        $scope.error_message = data.message;
		        $scope.error_flag = true;
		    }); 
		}
    }
}

function AddEditPurchaseInfoController($scope, $element, $http, $timeout, $location)
{
	$scope.error_flag = false;
	$scope.other_brand_flag = false;
	$scope.brand_flag = true;
	$scope.brand_val = '';
	$scope.init = function(csrf_token, user_id, purchase_id)
    {
        $scope.csrf_token = csrf_token;  
        $scope.user_id = user_id;
        $scope.purchase_id = purchase_id;
        $http.get('/fetch_brand_names/').success(function(data)
        {
            $scope.brands = data.brands;
            if ( data.brands.length > 0) {
            	$scope.other_brand_flag = false;
            } else {
            	$scope.other_brand_flag = true;
            }

        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });  
        $scope.brandname = 'select';
    }
    $scope.new_brand_name = function(){
    	if ($scope.brandname == 'others') {
    		$scope.other_brand_flag = true;
			$scope.brand_flag = false;
    	}
    }
    $scope.is_purchase_form_valid = function(){
    	if($scope.date == undefined || $scope.date == '') {
	        $scope.error_message = 'Please Enter Date';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.dealer_po_number == undefined || $scope.dealer_po_number == '') {
	        $scope.error_message = 'Please Enter Dealer PO Number';
	        $scope.error_flag = true;
	        return false;
	    } else if ($scope.invoice_no == undefined || $scope.invoice_no == '') {
	    	$scope.error_message = 'Please Enter Invoice Number';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.dealer_name == undefined || $scope.dealer_name == '') {
	        $scope.error_message = 'Please Enter Dealer Name';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.dealer_purchase_in_charge == undefined || $scope.dealer_purchase_in_charge == '') {
	        $scope.error_message = 'Please Enter Dealer Purchase in Charge';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.purchaser_sales_man == undefined || $scope.purchaser_sales_man == '') {
	        $scope.error_message = 'Please Enter Dealer Purchaseer Sales Man';
	        $scope.error_flag = true;
	        return false;
	    }
	    else if(($scope.brandname == undefined || $scope.brandname == '' || $scope.brandname == '? undefined:undefined ?') || ($scope.brandname == 'select')&& ($scope.new_brand == undefined || $scope.new_brand == '')) {
    		$scope.error_message = 'Please Choose or Add Brand Name';
	        $scope.error_flag = true;
	        return false;
	    } 
	    else if($scope.model == undefined || $scope.model == '' ) {
	    	$scope.error_message = 'Please Enter Model';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.address == undefined || $scope.address == '' ) {
	        $scope.error_message = 'Please Enter Address';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.contact_person == undefined || $scope.contact_person == '' ) {
	        $scope.error_message = 'Please Enter Contact Person';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.contact_no == undefined || $scope.contact_no == '' ) {
	        $scope.error_message = 'Please Enter Contact No';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.quantity == undefined || $scope.quantity == '' ) {
	        $scope.error_message = 'Please Enter Quantity';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.delivery_requested_date == undefined || $scope.delivery_requested_date == '' ) {
	        $scope.error_message = 'Please Enter Delivery Requested Date';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.installation_requested_date == undefined || $scope.installation_requested_date == '' ) {
	        $scope.error_message = 'Please Enter Installation Requested Date';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.extra_man_power == undefined || $scope.extra_man_power == '' ) {
	        $scope.error_message = 'Please Enter Extra Man Power';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.remarks == undefined || $scope.remarks == '' ) {
	        $scope.error_message = 'Please Enter Remarks';
	        $scope.error_flag = true;
	        return false;
	    }
	    return true;
    }
    $scope.add_purchase_info = function(){
    	$scope.is_valid = $scope.is_purchase_form_valid();
    	if ($scope.is_valid) {
    		if ($scope.brandname) {
		    	$scope.brand_val = $scope.brandname;
		    } else {
		    	$scope.brand_val = $scope.new_brand;
		    }
    		params = {
		    	'date': $scope.date,
		    	'dealer_po_number': $scope.dealer_po_number,
		    	'invoice_no': $scope.invoice_no,
		        'dealer_name': $scope.dealer_name,
		        'dealer_purchase_in_charge': $scope.dealer_purchase_in_charge,
		        'purchaser_sales_man': $scope.purchaser_sales_man,
		        'brand':$scope.brand_val,
		        'model':$scope.model,
		        'address':$scope.address,
		        'contact_person':$scope.contact_person,
		        'contact_no':$scope.contact_no,
		        'quantity':$scope.quantity,
		        'delivery_requested_date':$scope.delivery_requested_date,
		        'installation_requested_date':$scope.installation_requested_date,
		        'extra_man_power':$scope.extra_man_power,
		        'remarks':$scope.remarks,
		        "csrfmiddlewaretoken" : $scope.csrf_token
		    }
		    $http({
		        method : 'Post',
		        url : "/add_purchase_info/",
		        data : $.param(params),
		        headers : {
		        'Content-Type' : 'application/x-www-form-urlencoded'
		        }
		    }).success(function(data, status)
		    {
		        if(data.result == 'error'){
		            $scope.error_message = data.message;
		            $scope.error_flag = true;
		        } else {
		            document.location.href = '/';
		        }             
		    }).error(function(data, status)
		    {
		        $scope.error_message = data.message;
		        $scope.error_flag = true;
		    }); 
    	}
    }
    $scope.edit_purchase_info = function(){
    	params = {
	    	'delivery_requested_date':$scope.delivery_requested_date,
	        'installation_requested_date':$scope.installation_requested_date,
	        "csrfmiddlewaretoken" : $scope.csrf_token
	    }
	    $http({
	        method : 'Post',
	        url : "/purchase_info/"+$scope.purchase_id+'/',
	        data : $.param(params),
	        headers : {
	        'Content-Type' : 'application/x-www-form-urlencoded'
	        }
	    }).success(function(data, status)
	    {
	        if(data.result == 'error'){
	            $scope.error_message = data.message;
	            $scope.error_flag = true;
	        } else {
	        	console.log(data);
	            // document.location.href = '/';
	        }             
	    }).error(function(data, status)
	    {
	        $scope.error_message = data.message;
	        $scope.error_flag = true;
	    });
    }

}