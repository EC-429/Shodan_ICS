<h2>Shodan_ICS</h2>
<h4>Authored by: r_panov</h4>
<h5>'momentary masters of a fraction of a dot' - Carl Sagan</h5>


<p>
The Shodan_ICS repository has been created to assist in identifying public facing SCADA/ICS IT Assets connected to the internet. 
  
The Shodan_ICS python scripts can be utilized to display detailed information for each IP Address return by each Shodan search. This is done by calling the Shodan API and stripping/parsing the returned data. 

This project is coded in python3 and requires the following packages:<br>
`shodan            --> installation: pip3 install shodan`<br>
`sys               --> installation: pip3 install sys`<br>
`colorama          --> installation: pip3 install colorama`<br><br>

Download and run Shodan_ICS from command line:<br>
`git clone https://github.com/rpanov/Shodan_ICS.git`<br>
`$python3 IPEnumeration.py [shodan search]`<br>
`$python3 IPEnumeration_colored.py [shodan search]`<br>

Additionally, one can use the my compiled list of Shodan searches (i.e. Shodan_ICS_Searches.txt file) and the supplemental Vendor/product lists, to search generic ICS or SCADA assets:
- Shodan.io web interface 
- Shodan script with API Key.

Obviously, these searches and lists are not exhaustive of all possibilities and mileage will vary.

Please feel free to give advice, ideas, and opinions on how it can be improved!
Thanks.
</p>
