import random, time

class SentToAPI():
    def _retry_with_backoff(_send_to_api, max_attempts:int=5, seconds:int=1):
        def wrap(self, *args, **kwargs):
            attempt = 0 
            while True:
                try:
                    return _send_to_api(self)
                except:
                    if attempt == max_attempts:
                        print("Closing Connection...")                        
                        raise TimeoutError("TimeoutError: Number of attempts exceeded...")
                    else:
                        exponetial_time = (seconds * (2 ** attempt) + random.uniform(0,1))
                        print("Wating {}sec to retry...".format(exponetial_time))
                        time.sleep(exponetial_time)
                        attempt += 1
        return wrap

    @_retry_with_backoff(max_attempts=10, seconds=2)
    def _send_to_api(self):
        
        response, code, reason = get_response()

        if code == 200:
            print("All successful logs were inserted successfully")
        else:
            if code >= 300 and code < 500:
                print("All failed logs were inserted successfully")
            elif code >= 500:
                raise Exception("Server has response with a code 500. Trying to send request again...")

        print(f"Response code: {code}, {reason}")
        
        print("Closing Connection...")
        try:
            response.close()
            print("Connection Closed...")
        except Exception as ex:
            print(f"There was a problem closing the connection: \n\t{ex}")