function validateEmail(email) { 
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}

function get_day_name(day) {
	var weekday=new Array(7);
		weekday[0]="Sunday";
		weekday[1]="Monday";
		weekday[2]="Tuesday";
		weekday[3]="Wednesday";
		weekday[4]="Thursday";
		weekday[5]="Friday";
		weekday[6]="Saturday";
	var day_name = weekday[day]
	return day_name;
} 


function convert_to_date(date_val) {
	var date_value = date_val.split('-');
	var converted_date = new Date(date_value[2],date_value[1]-1, date_value[0]);
	return converted_date;
}

function get_difference_of_dates(date1, date2) {
	var date1 = convert_to_date(date1);
	var date2 = convert_to_date(date2);
	var diff = (date2 - date1)/(1000*60*60*24);
	return diff;
}

function delivery_requested_date_validation() {
	var delivery_date = $('#delivery_date').val();
	var delivery_dates = convert_to_date($('#delivery_date').val());
	var dt = new Date();
	var delivery_diff = (delivery_dates - dt)/(1000*60*60*24);
	if (delivery_diff <= 0) {
			if (dt.getHours() >= 12) {
			$('#express_delivery_message').html('Express delivery charge for the selected Delivery Requested Date is 200$')
			$('#is_express_delivery').show();
		} else {
			$('#express_delivery_message').html('Express delivery charge for the selected Delivery Requested Date is 400$')
			$('#is_express_delivery').show();
		}
	} else if (delivery_diff > 0 && delivery_diff <= 1) {
		$('#express_delivery_message').html('Express delivery charge for the selected Delivery Requested Date is 200$')
		$('#is_express_delivery').show();
	} else if (delivery_diff > 1 && delivery_diff <= 2) {
		$('#express_delivery_message').html('Express delivery charge for the selected Delivery Requested Date is 100$')
		$('#is_express_delivery').show();
	} else {
		$('#express_delivery_message').html('Express delivery charge for the selected Delivery Requested Date is 100$')
		$('#is_express_delivery').hide();
	}
}

function edit_delivery_requested_date_validation() {
	var purchase_date = $('#date').val();
	var purchase_dates = convert_to_date($('#date').val());
	var delivery_date = $('#delivery_date').val();
	var delivery_dates = convert_to_date($('#delivery_date').val());
	var date_change_count = $('#delivery_date_changes').val();
	var dt = new Date();
	date_change_count = parseInt(date_change_count) + 1;
	var date_change_charge = date_change_count * 30
	diff = (delivery_dates - dt)/(1000*60*60*24);
	if ((delivery_dates.getDate() == dt.getDate() && delivery_dates.getMonth() == dt.getMonth() && delivery_dates.getYear() == dt.getYear()) || diff > 0) {
		
		if (purchase_dates.getDate() == dt.getDate() && purchase_dates.getMonth() == dt.getMonth() && purchase_dates.getYear() == dt.getYear()) {
			var delivery_diff = (delivery_dates - dt)/(1000*60*60*24);
			if (delivery_diff <= 0) {
				if (dt.getHours() >= 12) {
					$('#express_delivery_message').html('Express delivery charge for the selected Delivery Requested Date is 200$ and the Date change charge is '+date_change_charge+'$')
					$('#is_express_delivery').show();
				} else {
					$('#express_delivery_message').html('Express delivery charge for the selected Delivery Requested Date is 400$ and the Date change charge is '+date_change_charge+'$')
					$('#is_express_delivery').show();
				}
			} else if (delivery_diff > 0 && delivery_diff <= 1) {
				$('#express_delivery_message').html('Express delivery charge for the selected Delivery Requested Date is 200$ and the Date change charge is '+date_change_charge+'$')
				$('#is_express_delivery').show();
			} else if (delivery_diff > 1 && delivery_diff <= 2) {
				$('#express_delivery_message').html('Express delivery charge for the selected Delivery Requested Date is 100$ and the Date change charge is '+date_change_charge+'$')
				$('#is_express_delivery').show();
			} else {
				$('#express_delivery_message').html('The Date change charge is '+date_change_charge+'$')
				$('#is_express_delivery').show();
			}
		} else {
			var delivery_diff = (delivery_dates - purchase_dates)/(1000*60*60*24);
			if (delivery_diff <= 0) {
				$('#express_delivery_message').html('Express delivery charge for the selected Delivery Requested Date is 400$ and the Date change charge is '+date_change_charge+'$')
				$('#is_express_delivery').show();
			} else if (delivery_diff > 0 && delivery_diff <= 1) {
				$('#express_delivery_message').html('Express delivery charge for the selected Delivery Requested Date is 200$ and the Date change charge is '+date_change_charge+'$')
				$('#is_express_delivery').show();
			} else if (delivery_diff > 1 && delivery_diff <= 2) {
				$('#express_delivery_message').html('Express delivery charge for the selected Delivery Requested Date is 100$ and the Date change charge is '+date_change_charge+'$')
				$('#is_express_delivery').show();
			} else {
				$('#express_delivery_message').html('The date change charge is '+date_change_charge+'$')
				$('#is_express_delivery').show();
			}
		}
	} else if (diff < 0){
		$('#express_delivery_message').html('Please choose a date greater than or equal to todays date');
		$('#is_express_delivery').show();
	}
}

function edit_installation_requested_date_validation() {
	var purchase_date = $('#date').val();
	var purchase_dates = convert_to_date($('#date').val());
	var installed_date = $('#installation_date').val();
	var installed_dates = convert_to_date($('#installation_date').val());
	var date_change_count = $('#installation_date_change').val();
	date_change_count = parseInt(date_change_count) + 1;
	var date_change_charge = date_change_count * 30
	var dt = new Date();
	diff = (installed_dates - dt)/(1000*60*60*24);
	if ((installed_dates.getDate() == dt.getDate() && installed_dates.getMonth() == dt.getMonth() && installed_dates.getYear() == dt.getYear()) || diff > 0) {
		
		if (purchase_dates.getDate() == dt.getDate() && purchase_dates.getMonth() == dt.getMonth() && purchase_dates.getYear() == dt.getYear()) {
			var installed_diff = (installed_dates - dt)/(1000*60*60*24);
			if (installed_diff <= 0) {
				if (dt.getHours() >= 12) {
					$('#express_installation_message').html('Express delivery charge for the selected Installation Requested Date is 200$ and the Date change charge is '+date_change_charge+'$')
					$('#is_express_installation').show();
				} else {
					$('#express_installation_message').html('Express delivery charge for the selected Installation Requested Date is 400$ and the Date change charge is '+date_change_charge+'$')
					$('#is_express_installation').show();
				}
			} else if (installed_diff > 0 && installed_diff <= 1) {
				$('#express_installation_message').html('Express Installation charge for the selected Installation Requested Date is 200$ and the Date change charge is '+date_change_charge+'$')
				$('#is_express_installation').show();
			} else if (installed_diff > 1 && installed_diff <= 2) {
				$('#express_installation_message').html('Express Installation charge for the selected Installation Requested Date is 100$ and the Date change charge is '+date_change_charge+'$')
				$('#is_express_installation').show();
			} else {
				$('#is_express_installation').show();
				$('#express_installation_message').html('The Date change charge is '+date_change_charge+'$')
			}
		} else {
			var installed_diff = (installed_dates - purchase_dates)/(1000*60*60*24);
			if (installed_diff <= 0) {
				$('#express_installation_message').html('Express Installation charge for the selected Installation Requested Date is 400$ and the Date change charge is '+date_change_charge+'$')
				$('#is_express_installation').show();
				
			} else if (installed_diff > 0 && installed_diff <= 1) {
				$('#express_installation_message').html('Express Installation charge for the selected Installation Requested Date is 200$ and the Date change charge is '+date_change_charge+'$')
				$('#is_express_installation').show();
			} else if (installed_diff > 1 && installed_diff <= 2) {
				$('#express_installation_message').html('Express Installation charge for the selected Installation Requested Date is 100$ and the Date change charge is '+date_change_charge+'$')
				$('#is_express_installation').show();
			} else {
				$('#is_express_installation').show();
				$('#express_installation_message').html('The Date change charge is '+date_change_charge+'$')
			}
		}
	} else if (diff < 0){
		$('#express_installation_message').html('Please choose a date greater than or equal to todays date');
		$('#is_express_installation').show();
	}
}

function installation_requested_date_validation() {
	var installed_date = $('#installation_date').val();
	var installed_dates = convert_to_date($('#installation_date').val());
	var dt = new Date();
	var installed_diff = (installed_dates - dt)/(1000*60*60*24);
	if (installed_diff <= 0) {
			if (dt.getHours() >= 12) {
			$('#express_installation_message').html('Express Installation charge for the selected Installation Requested Date is 200$')
			$('#is_express_installation').show();
		} else {
			$('#express_installation_message').html('Express Installation charge for the selected Installation Requested Date is 400$')
			$('#is_express_installation').show();
		}
	} else if (installed_diff > 0 && installed_diff <= 1) {
		$('#express_installation_message').html('Express Installation charge for the selected Installation Requested Date is 200$')
		$('#is_express_installation').show();
	} else if (installed_diff > 1 && installed_diff <= 2) {
		$('#express_installation_message').html('Express Installation charge for the selected Installation Requested Date is 100$')
		$('#is_express_installation').show();
	} else {
		$('#is_express_installation').hide();
	}
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
    } else if($scope.user_type == 'customer/dealer') {
    	if ($scope.dealer_company_name == '' || $scope.dealer_company_name == undefined) {
    		$scope.error_message = 'Please Enter Dealer Company Name';
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
	$scope.is_dealer = false;
	$scope.is_express_delivery = false;
	$scope.init = function(csrf_token)
    {
        $scope.csrf_token = csrf_token; 
        $scope.user_type = 'select';    
    }
    $scope.is_user_type_vendor = function(){
    	if ($scope.user_type == 'vendors') {
    		$scope.is_vendor = true;
    		$scope.is_dealer = false;
    	} else if ($scope.user_type == 'customer/dealer') {
    		$scope.is_dealer = true;
    		$scope.is_vendor = false;
    	} else {
    		$scope.is_vendor = false;
    		$scope.is_dealer = false;
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
		        'dealer_name': $scope.dealer_company_name,
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

function AddSubDealerController($scope, $element, $http, $timeout, $location)
{
	$scope.error_flag = false;
	$scope.is_dealer_customer = false;
	$scope.init = function(csrf_token, user_id)
    {
        $scope.csrf_token = csrf_token;  
        $scope.user_id = user_id;
        $scope.user_type = 'select';
    }
    $scope.add_subdealer = function (){
    	$scope.is_valid = register_form_validation($scope);
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
	$scope.other_purchase_sales_man_flag = false;
	$scope.purchase_sales_man_flag = true;
	$scope.dealer_flag = true;
	$scope.other_dealer_flag = false;
	$scope.brand_val = '';
	$scope.dealer_sales_man = '';
	$scope.dealer_purchaser = '';
	$scope.date = '';
	$scope.delivery_requested_date = ''; 
	$scope.installation_requested_date = '';
	$scope.express_delivery_msg = '';
	$scope.express_installation_delivery_msg = '';
	$('#is_express_delivery').hide();
	$scope.init = function(csrf_token, user_id, user_type ,purchase_id)
    {
        $scope.csrf_token = csrf_token;  
        $scope.user_id = user_id;
        $scope.user_type = user_type;
        $scope.purchase_id = purchase_id;
        
        $http.get('/fetch_brand_names/').success(function(data)
        {
            if ( data.brands.length > 0) {
            	$scope.brands = data.brands;
            	$scope.other_brand_flag = false;
            } else {
            	$scope.other_brand_flag = true;
            }

        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });  
        $scope.brandname = 'select';

        $http.get('/fetch_purchase_sales_men/').success(function(data)
        {
            if ( data.purchase_sales_men.length > 0) {
            	$scope.purchase_sales_men = data.purchase_sales_men;
            	$scope.other_purchase_sales_man_flag = false;
            } else {
            	$scope.other_purchase_sales_man_flag = true;
            }

        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });  
        $scope.existing_purchase_sales_man = 'select';

        $http.get('/fetch_dealers/').success(function(data)
        {
            if ( data.dealers.length > 0) {
            	$scope.dealers = data.dealers;
            	$scope.other_dealer_flag = false;
            } else {
            	$scope.other_dealer_flag = true;
            }

        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });  
        $scope.dealers_name = 'select';
        $http.get('/fetch_dealer_company_names/').success(function(data)
        {
        	$scope.is_dealer_customer = data.is_dealer;
            if (!(data.is_dealer)) {
            	$scope.dealer_company_names = data.dealer_company_names;
            	$scope.is_dealer_flag = false;
            	$scope.not_dealer_flag = true;
            	$scope.not_dealer_name = 'select';
            } else {
            	$scope.is_dealer_flag = true;
            	$scope.firm_name = data.dealer_company_names;
            	$scope.not_dealer_name = 'select';
            }


        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });  
        $scope.dealers_name = 'select';
    }

    $scope.add_new_brand_name = function(){
    	if ($scope.brandname == 'others') {
    		$scope.other_brand_flag = true;
			$scope.brand_flag = false;
    	}
    }
    $scope.add_new_purchase_sales_man = function() {
    	if ($scope.existing_purchase_sales_man == 'others') {
    		$scope.other_purchase_sales_man_flag = true;
			$scope.purchase_sales_man_flag = false;
    	}
    }
    $scope.add_new_dealer = function() {
    	if ($scope.dealers_name == 'others') {
    		$scope.other_dealer_flag = true;
			$scope.dealer_flag = false;
    	}
    }
    $scope.add_new_firm = function() {
    	if ($scope.not_dealer_name == 'others') {
    		$scope.is_dealer_flag = true;
			$scope.not_dealer_flag = false;
    	}
    }
    $scope.is_purchase_form_valid = function(){
    	$scope.is_express_delivery = false;
    	$scope.date = $('#date').val();
    	$scope.delivery_requested_date = $('#delivery_date').val();
		$scope.installation_requested_date = $('#installation_date').val();

		// Date validation 1) Check the entered date belongs to Sunday or Saturday , 2) Check the installation date is less than the delivery date
		var delivery_dates = convert_to_date($('#delivery_date').val());
		var delivery_dates_day_name = get_day_name(delivery_dates.getDay());
		var installation_dates = convert_to_date($('#installation_date').val());
		var installation_dates_day_name = get_day_name(installation_dates.getDay());
		var purchase_date = convert_to_date($('#date').val());
		if($scope.date == undefined || $scope.date == '') {
	        $scope.error_message = 'Please Enter Date';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.dealer_po_number == undefined || $scope.dealer_po_number == '') {
	        $scope.error_message = 'Please Enter Dealer PO Number';
	        $scope.error_flag = true;
	        return false;
	    } else if ($scope.delivery_order_number == undefined || $scope.delivery_order_number == '') {
	    	$scope.error_message = 'Please Enter Delivery Order Number';
	        $scope.error_flag = true;
	        return false;
	    } 
	    else if(($scope.not_dealer_name == undefined || $scope.not_dealer_name == '' || $scope.not_dealer_name == '? undefined:undefined ?' || (($scope.not_dealer_name == 'select' ) && ($scope.firm_name == undefined || $scope.firm_name == ''))) || (($scope.not_dealer_name == 'others')&&($scope.firm_name == undefined || $scope.firm_name == '')) || (($scope.is_dealer_flag==true && ($scope.firm_name == undefined || $scope.firm_name == '')))) {
	        $scope.error_message = 'Please Choose or Add Dealer/Company Name';
	        $scope.error_flag = true;
	        return false;
	    }
	    else if(($scope.dealers_name == undefined || $scope.dealers_name == '' || $scope.dealers_name == '? undefined:undefined ?' || (($scope.dealers_name == 'select' ) && ($scope.new_dealer == undefined || $scope.new_dealer == ''))) || (($scope.dealers_name == 'others')&&($scope.new_dealer == undefined || $scope.new_dealer == ''))) {
	        $scope.error_message = 'Please Choose or Add Dealer Purchaser';
	        $scope.error_flag = true;
	        return false;
	    } else if(($scope.existing_purchase_sales_man == undefined || $scope.existing_purchase_sales_man == '' || $scope.existing_purchase_sales_man == '? undefined:undefined ?' || (($scope.existing_purchase_sales_man == 'select') && ($scope.new_purchase_sales_man == undefined || $scope.new_purchase_sales_man == ''))) || (($scope.existing_purchase_sales_man == 'others') && ($scope.new_purchase_sales_man == undefined || $scope.new_purchase_sales_man == ''))) {
	        $scope.error_message = 'Please Choose or Add Dealer Sales Man';
	        $scope.error_flag = true;
	        return false;
	    } else if(($scope.brandname == undefined || $scope.brandname == '' || $scope.brandname == '? undefined:undefined ?' || (($scope.brandname == 'select') && ($scope.new_brand == undefined || $scope.new_brand == ''))) || (($scope.brandname == 'others')&& ($scope.new_brand == undefined || $scope.new_brand == ''))) {
    		$scope.error_message = 'Please Choose or Add Brand Name';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.model == undefined || $scope.model == '' ) {
	    	$scope.error_message = 'Please Enter Model';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.customer == undefined || $scope.customer == '' ) {
	        $scope.error_message = 'Please Enter Customer';
	        $scope.error_flag = true;
	        return false;
	    } else if ($scope.telephone_no == undefined || $scope.telephone_no == '') {
	    	$scope.error_message = 'Please Enter Telephone Number';
	        $scope.error_flag = true;
	        return false;
        } else if ($scope.mobile_no == undefined || $scope.mobile_no == '') {
	    	$scope.error_message = 'Please Enter Mobile Number';
	        $scope.error_flag = true;
	        return false;
        } else if($scope.block_house_no == undefined || $scope.block_house_no == '' ) {
	        $scope.error_message = 'Please Enter Block or House No';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.floor_no == undefined || $scope.floor_no == '' ) {
	        $scope.error_message = 'Please Enter Floor No';
	        $scope.error_flag = true;
	        return false;
	    } else if ($scope.unit_no == undefined || $scope.unit_no == '') {
	    	$scope.error_message = 'Please Enter Unit No';
	        $scope.error_flag = true;
	        return false;
	    } else if ($scope.building_name == undefined || $scope.building_name == '') {
	    	$scope.error_message = 'Please Enter Building Name';
	        $scope.error_flag = true;
	        return false;
	    } else if ($scope.street_name == undefined || $scope.street_name == '') {
	    	$scope.error_message = 'Please Enter Street Name';
	        $scope.error_flag = true;
	        return false;
	    } else if ($scope.postal_code == undefined || $scope.postal_code == '') {
	    	$scope.error_message = 'Please Enter Postal Code';
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
	    } else if (delivery_dates < purchase_date) {
	    	$scope.error_message = 'Delivery Requested Date should be greater than or equal to the Purchase date';
	        $scope.error_flag = true;
	        return false;
		} else if(delivery_dates_day_name == 'Sunday' || delivery_dates_day_name == 'Saturday') {
	    	$scope.error_message = 'Entered Delivery Requested Date is a '+delivery_dates_day_name;
	    	$scope.error_flag = true;
	    	return false;
	    } else if($scope.installation_requested_date == undefined || $scope.installation_requested_date == '' ) {
	        $scope.error_message = 'Please Enter Installation Requested Date';
	        $scope.error_flag = true;
	        return false;
	    } else if (installation_dates < delivery_dates) {
	    	$scope.error_message = 'Installation Requested Date should be greater than or equal to the Delivery Requested Date';
	        $scope.error_flag = true;
	        return false;
		} else if(installation_dates_day_name == 'Sunday' || installation_dates_day_name == 'Saturday') {
	    	$scope.error_message = 'Entered Installation Requested Date is a '+installation_dates_day_name;
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
    		$scope.error_flag = false;
    		$scope.is_express_delivery = false;
    		if ($scope.brandname == 'others' || $scope.brandname == 'select') {
		    	$scope.brand_val = $scope.new_brand;
		    } else {
		    	$scope.brand_val = $scope.brandname;
		    }
		    if ($scope.existing_purchase_sales_man == 'others' || $scope.existing_purchase_sales_man == 'select') {
		    	$scope.dealer_sales_man = $scope.new_purchase_sales_man;
		    } else {
		    	$scope.dealer_sales_man = $scope.existing_purchase_sales_man;
		    }
		    if ($scope.dealers_name == 'others' || $scope.dealers_name == 'select') {
		    	$scope.dealer_purchaser = $scope.new_dealer;
		    } else {
		    	$scope.dealer_purchaser = $scope.dealers_name;
		    }
		    if ($scope.is_dealer_customer || $scope.not_dealer_name == 'others' || $scope.not_dealer_name == 'select') {
				$scope.dealer_company_name = $scope.firm_name;
			} else {
				$scope.dealer_company_name = $scope.not_dealer_name;
			}

			params = {
		    	'date': $scope.date,
		    	'dealer_po_number': $scope.dealer_po_number,
		    	'delivery_order_number': $scope.delivery_order_number,
		        'dealer_company_name': $scope.dealer_company_name,
		        'dealer_purchaser': $scope.dealer_purchaser,
		        'dealer_sales_man': $scope.dealer_sales_man,
		        'brand':$scope.brand_val,
		        'model':$scope.model,
		        'customer':$scope.customer,
		        'block_house_no': $scope.block_house_no,
		        'floor_no': $scope.floor_no,
		        'unit_no': $scope.unit_no,
		        'building_name': $scope.building_name,
		        'street_name': $scope.street_name,
		        'postal_code': $scope.postal_code,
		        'telephone_no': $scope.telephone_no,
		        'mobile_no': $scope.mobile_no,
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
		        } 
		        else {
		            document.location.href = '/';
		        }             
		    }).error(function(data, status)
		    {
		        $scope.error_message = data.message;
		        $scope.error_flag = true;
		    }); 
    	}
    }
    $scope.is_edit_purchase_form_valid = function(){
    	$scope.is_express_delivery = false;
    	$scope.date = $('#date').val();
    	$scope.delivery_requested_date = $('#delivery_date').val();
		$scope.installation_requested_date = $('#installation_date').val();
		$scope.extra_man_power = $('#extra_man_power').val();
		$scope.delivery_order_number = $('#delivery_order_number').val();
		$scope.dealer_sales_man = $('#dealer_sales_man').val();
		$scope.brand_val = $('#brand').val();
		$scope.model = $('#model').val();
		$scope.customer = $('#customer').val();
		$scope.telephone_no = $('#telephone_number').val();
		$scope.mobile_no = $('#mobile_number').val();
		$scope.block_house_no = $('#block_house_number').val();
		$scope.floor_no = $('#floor_number').val();
		$scope.unit_no = $('#unit_number').val();
		$scope.building_name = $('#building_name').val();
		$scope.street_name = $('#street_name').val();
		$scope.postal_code = $('#postal_code').val();
		$scope.quantity = $('#quantity').val();
		$scope.remarks = $('#remarks').val();
		$scope.dealer_po_number = $('#delivery_po_number').val();
		$scope.dealer_company_name = $('#dealer_company_name').val();
		$scope.dealer_purchaser = $('#dealer_purchaser').val();
		// Date validation 1) Check the entered date belongs to Sunday or Saturday , 2) Check the installation date is less than the delivery date
		
		var delivery_dates = convert_to_date($('#delivery_date').val());
		var delivery_dates_day_name = get_day_name(delivery_dates.getDay());
		var installation_dates = convert_to_date($('#installation_date').val());
		var installation_dates_day_name = get_day_name(installation_dates.getDay());
		var purchase_date = convert_to_date($('#date').val());

		if ($scope.delivery_order_number == undefined || $scope.delivery_order_number == '') {
	    	$scope.error_message = 'Please Enter Delivery Order Number';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.dealer_sales_man == undefined || $scope.dealer_sales_man == '') {
	        $scope.error_message = 'Dealer Sales Man cannot be null';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.brand_val == undefined || $scope.brand_val == '') {
    		$scope.error_message = 'Brand Name cannot be null';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.model == undefined || $scope.model == '' ) {
	    	$scope.error_message = 'Please Enter Model';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.customer == undefined || $scope.customer == '' ) {
	        $scope.error_message = 'Please Enter Customer';
	        $scope.error_flag = true;
	        return false;
	    } else if ($scope.telephone_no == undefined || $scope.telephone_no == '') {
	    	$scope.error_message = 'Please Enter Telephone Number';
	        $scope.error_flag = true;
	        return false;
        } else if ($scope.mobile_no == undefined || $scope.mobile_no == '') {
	    	$scope.error_message = 'Please Enter Mobile Number';
	        $scope.error_flag = true;
	        return false;
        } else if($scope.block_house_no == undefined || $scope.block_house_no == '' ) {
	        $scope.error_message = 'Please Enter Block or House No';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.floor_no == undefined || $scope.floor_no == '' ) {
	        $scope.error_message = 'Please Enter Floor No';
	        $scope.error_flag = true;
	        return false;
	    } else if ($scope.unit_no == undefined || $scope.unit_no == '') {
	    	$scope.error_message = 'Please Enter Unit No';
	        $scope.error_flag = true;
	        return false;
	    } else if ($scope.building_name == undefined || $scope.building_name == '') {
	    	$scope.error_message = 'Please Enter Building Name';
	        $scope.error_flag = true;
	        return false;
	    } else if ($scope.street_name == undefined || $scope.street_name == '') {
	    	$scope.error_message = 'Please Enter Street Name';
	        $scope.error_flag = true;
	        return false;
	    } else if ($scope.postal_code == undefined || $scope.postal_code == '') {
	    	$scope.error_message = 'Please Enter Postal Code';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.quantity == undefined || $scope.quantity == '' ) {
	        $scope.error_message = 'Please Enter Quantity';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.remarks == undefined || $scope.remarks == '' ) {
	        $scope.error_message = 'Please Enter Remarks';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.dealer_po_number == undefined || $scope.dealer_po_number == '') {
	        $scope.error_message = 'Please Enter Dealer PO Number';
	        $scope.error_flag = true;
	        return false;dealer_company_name
	    } else if($scope.dealer_company_name == undefined || $scope.dealer_company_name == '') {
	        $scope.error_message = 'Dealer/Company Name cannot be null';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.dealer_purchaser == undefined || $scope.dealer_purchaser == '') {
	        $scope.error_message = 'Dealer Purchaser cannot be null';
	        $scope.error_flag = true;
	        return false;
	    } else if($scope.delivery_requested_date == undefined || $scope.delivery_requested_date == '' ) {
	        $scope.error_message = 'Please Enter Delivery Requested Date';
	        $scope.error_flag = true;
	        return false;
	    } else if (delivery_dates < purchase_date) {
	    	$scope.error_message = 'Delivery Requested Date should be greater than or equal to the Purchase date';
	        $scope.error_flag = true;
	        return false;
		} else if(delivery_dates_day_name == 'Sunday' || delivery_dates_day_name == 'Saturday') {
	    	$scope.error_message = 'Entered Delivery Requested Date is a '+delivery_dates_day_name;
	    	$scope.error_flag = true;
	    	return false;
	    } else if($scope.installation_requested_date == undefined || $scope.installation_requested_date == '' ) {
	        $scope.error_message = 'Please Enter Installation Requested Date';
	        $scope.error_flag = true;
	        return false;
	    } else if (installation_dates < delivery_dates) {
	    	$scope.error_message = 'Installation Requested Date should be greater than or equal to the Delivery Requested Date';
	        $scope.error_flag = true;
	        return false;
		} else if(installation_dates_day_name == 'Sunday' || installation_dates_day_name == 'Saturday') {
	    	$scope.error_message = 'Entered Installation Requested Date is a '+installation_dates_day_name;
	    	$scope.error_flag = true;
	    	return false;
	    } else if($scope.extra_man_power == undefined || $scope.extra_man_power == '' ) {
	        $scope.error_message = 'Please Enter Extra Man Power';
	        $scope.error_flag = true;
	        return false;
	    }
	    return true;

    }
    $scope.edit_purchase_info = function(){
    	$scope.is_valid = $scope.is_edit_purchase_form_valid();
    	if ($scope.is_valid) {
    		$scope.error_flag = false;
    		$scope.delivery_status = $('#delivery_status').val();
    		$scope.installed_status = $('#installed_status').val();
    		params = {
    			'delivery_order_number': $scope.delivery_order_number,
		        'dealer_sales_man': $scope.dealer_sales_man,
		        'brand':$scope.brand_val,
		        'model':$scope.model,
		        'customer':$scope.customer,
		        'block_house_no': $scope.block_house_no,
		        'floor_no': $scope.floor_no,
		        'unit_no': $scope.unit_no,
		        'building_name': $scope.building_name,
		        'street_name': $scope.street_name,
		        'postal_code': $scope.postal_code,
		        'telephone_no': $scope.telephone_no,
		        'mobile_no': $scope.mobile_no,
		        'quantity':$scope.quantity,
		        'delivery_requested_date':$scope.delivery_requested_date,
		        'installation_requested_date':$scope.installation_requested_date,
		        'extra_man_power_request': $scope.extra_man_power,
		        
		        'dealer_po_number': $scope.dealer_po_number,
		    	'dealer_company_name': $scope.dealer_company_name,
		        'dealer_purchaser': $scope.dealer_purchaser,
		        
		        'delivery_status': $scope.delivery_status,
		        'installed_status': $scope.installed_status,
		        'remarks':$scope.remarks,
		        "csrfmiddlewaretoken" : $scope.csrf_token
		    }
		    $http({
		        method : 'Post',
		        url : "/purchase_info/"+$scope.purchase_id+"/",
		        data : $.param(params),
		        headers : {
		        'Content-Type' : 'application/x-www-form-urlencoded'
		        }
		    }).success(function(data, status)
		    {
		        if(data.result == 'error'){
		            $scope.error_message = data.message;
		            $scope.error_flag = true;
		        } 
		        else {
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

function HomeController($scope, $element, $http, $timeout, $location)
{
	$scope.error_flag = false;
	$scope.init = function(csrf_token)
    {
        $scope.csrf_token = csrf_token;  
    }
    $scope.search_purchase_info = function (){
    	document.location.href ='/search_purchase_info/'+$scope.delivery_order_number+'/';
    }
}