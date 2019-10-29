from requests import Session
import time, datetime

def now_milliseconds():
   return int(time.time() * 1000)

# reference time.time
# Return the current time in seconds since the Epoch.
# Fractions of a second may be present if the system clock provides them.
# Note: if your system clock provides fractions of a second you can end up 
# with results like: 1405821684785.2 
# our conversion to an int prevents this

def date_time_milliseconds(date_time_obj):
   return int(time.mktime(date_time_obj.timetuple()) * 1000)

# reference: time.mktime() will
# Convert a time tuple in local time to seconds since the Epoch.

mstimeone = now_milliseconds()

mstimetwo = date_time_milliseconds(datetime.datetime.utcnow())

session = Session()

# HEAD requests ask for *just* the headers, which is all you need to grab the
# session cookie
session.head('http://www.fip.it')


'''
$.ajax({
			type: "POST",
			cache: false,
			url: "FipWeb/ajaxRisultatiGetPartite.aspx?" + new Date().getTime(),
			data: ""
					+ "com=" + encodeURIComponent(Comitato)
					+ "&sesso=" + encodeURIComponent(Sesso)
					+ "&camp=" + encodeURIComponent(Campionato)
					+ "&fase=" + encodeURIComponent(Fase)
					+ "&girone=" + encodeURIComponent(Girone)
					+ "&ar=" + encodeURIComponent(AR)
					+ "&turno=" + encodeURIComponent(Turno)
					+ "&IDRegione=" + encodeURIComponent(IDRegione)
					+ "&IDProvincia=" + encodeURIComponent(IDProvincia)
					+ "&reload=" + encodeURIComponent(reload),
			dataType: "html",
			success: function(returnHtml) {
				$('#content-risultati-partite').html(returnHtml);
			},
			error: function(xhr, status, error) {
				console.log("ajax error getRisultatiPartite(): " + error);
			}
		});
'''


#http://www.fip.it/risultati.aspx?com=RTN&sesso=M&camp=D&fase=1&girone=39727&ar=1&turno=5&IDRegione=TN&IDProvincia=TN

#getRisultatiPartite("RTN", "M", "D", "1", "39727", "1", "5", "TN", "TN", "");

response = session.post(
    url = "FipWeb/ajaxRisultatiGetPartite.aspx?" + str(mstimetwo),
    data = {
        '&com': 'RTN',
        '&sesso': 'M',
        '&camp': 'D',
        '&fase': '1',
        '&girone' :'39727',
        '&ar': '1',
        '&turno': '5',
        '&IDRegione': 'TN',
        '&IDProvincia': 'TN',
        '&reload': ''    
    }
)
                    


'''
response = session.post(
    url='http://sportsbeta.ladbrokes.com/view/EventDetailPageComponentController',
    data={
        'N': '4294966750',
        'form-trigger': 'moreId',
        'moreId': '156#327',
        'pageType': 'EventClass'
    },
    headers={
        'Referer': 'http://sportsbeta.ladbrokes.com/football'
    }
)
'''

print(response.text)