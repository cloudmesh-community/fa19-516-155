# Datacenter fa19-516-155

## E.Datacenter.2.a: Carbon footprint of data centers  

* Table updated at :  
'<https://docs.google.com/spreadsheets/d/1gh869zfjA4sVxL8-ga0af2_HLTTuOoD1IReuRSrbq4I/edit#gid=0>'  


## E.Datacenter.2.b: Carbon footprint of data centers

* Data center   : Prineville, OR
* Organization  : Facebook
* Location      : Prineville, OR
* Year Build    : 2011

Facebook targets 100% usage of renewable energy by 2020. In 2018, this
percentage was 75%. Following are the details of 2018 data:

Total energy consumption of the data center was 488,000 MWh in the year
2018, which translates to 55707.76 kW [@www-facebook-sustainability-report].

Using following formula the 'IT load' comes out to be:

* PUE = Total facility energy / IT equipment energy  
* 1.11 = 55707.76 /  IT equipment energy  
* IT equipment energy =  50,187.17 kW  

Electricity cost in Prineville, OR is $ 0.09/kWh. Maximum available
value of the IT load in the Schneider carbon foot print calculator is
1/5th of the above load. Hence using 10,000 kW as the IT load and then
multiplying the results by 5 we get following results -

|Attribute                     |Value  |
|------------------------------|:-----:|
|Electricity Cost (\$/kW) | 0.09  |  
|IT Load (kW) | 50,187.17 kW  |  
|Yearly Cost ($) | 43.35 M  |  
|Yearly CO2 Footprint(tons)  | 58,394  |  
|CO2 equivalent in cars|12,873  |  

Facebook has provided an interesting visualization which shows variation
in PUE of this data center in an interactive manner [@www-facebook-PrinevilleDataCente-app]:

![Facebook Prineville Datacenter [@www-facebook-PrinevilleDataCente-app]](images/FB_Prineville_DataCenter_PUE.png){#fig:FB_Prineville_DataCenter_PUE}

### References

1. [@www-Sustaina48] <https://sustainability.fb.com/sustainability-in-numbers/>  
2. [@www-2018Sust40] <https://sustainability.fb.com/wp-content/uploads/2019/08/2018-Sustainability-Data-Disclosure.pdf>  
3. [@www-42Prinev26] <https://www.facebook.com/PrinevilleDataCenter/app/399244020173259/>  
4. [@www-Sustaina54] <https://sustainability.fb.com/sustainability-in-numbers/#section-GreenhouseGasEmissions>


## E.Datacenter.3: Your own Carbon footprint  

My Footprint `11927 lbs of CO2`  


## E.Datacenter.4: Thermal energy usage at Data Centers

* Thermal energy the energy available in the form of heat. It is
  utilized by convection, conduction or radiation. Examples of thermal
  energies are solar thermal energy, geothermal energy.
* Thermal energy can be converted in electricity and used for data
  center usage. Another way of using thermal energy is by recycling
  the head generated by data center and using it for various purposes
  such as heating residential or industrial areas.
* Thermal energy made available by data centers in this way,
  indirectly reduce usage of the conventional fuels for heating
  purposes.
* An interesting example of such reuse of thermal energy is observed
  at the **Facebook datacenter of Odense, Denmark** [@www-WasteHea35]. This data center
  has deployed waste heat recovery system that captures the excess
  heat generated by data centers and then distributes it to the local
  community using a heat pump.
* This is thermal energy is used for heating of local houses reducing
  dependency on conventional energy sources. This also helps to reduce
  greenhouse gas emission.
* Heat captured at the data center is conducted to local houses
  through district heating network.
* Best part is that this data center itself is also powered by
  renwable wind energy.

### References 

1. [@www-Sustaina73] <https://sustainability.fb.com/innovation-for-our-world/sustainable-data-centers/>  


## E.Datacenter.5: Efforts towards renewable energy

* Continuing the example of **Facebook datacenter of Odense,
  Denmark** [@www-WasteHea35], this center uses wind energy instead of conventional
  energy sources demonstrating Facebook's efforts toward renewable
  energy.
* In addition to this, this data center also employs a excess heat
  recovery system which captures and recycles the heat generated by
  data center cooling process.
* This captured thermal energy is transferred to district heating
  network where it is put to good use by local houses.
* Denamrk has a national goal to phase out coal usage by 2030. By
  using the thermal energy generated by data center Odense city hopes
  to achieve this goal by 2025 itself.
* Once fully functional, this data center aims to save 100,000 MWh of
  energy per year.


## E.Datacenter.8: Data center outage

This is a summary of a data center outage effecting AWS3 
[@www-AWSS3Out51] 
[@www-Howatypo27].

* Data center outages occur due to reasons ranging for power supply
  failures to natural calamities. Such outages disable one or many
  services provided by the data center causing unavailability of
  services relied on such data center.
* One such curious case occurred on Feb 28th, 2017 at AWS US-East-1
  data center in Ashburn, Virginia.
* This outage mainly **affected S3 service on US-East-1** region of
  Amazon Web Services.
* Affected AWS S3 service was in use by oranganizations such as Quora,
  Coursera, Docker, Medium. As these are all customer facing services,
  the impact of this outage was directly felt by the end users.
* This is a peculiar case of data center outage because it was in fact
  **cuase**ed by **human error**. As later investigated by AWS, it was
  found out that while analizing an issue in the billing system, the
  technical team brough down unexpected number of servers. Which led
  to unavailability of varios other services. A complete restart was
  required in order to restore all these services. This increased the
  down time of dependant services.
* Details of the impact of this outage in dollars was not found.
* Since then Amazon has implemented multiple methods **to avoid** this
  scenario in future. Few of such methos include greater control on
  human errors, improvement of the avaialbility monitoring system and
  setting up a threshold value below which the technical team won't be
  able to bring down any server capacity.

