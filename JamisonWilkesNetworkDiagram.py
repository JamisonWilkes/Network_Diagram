#Jamison Wilkes
#Network Diagram Lab

import ipaddress

ipInterface = ipaddress.ip_interface('138.191.0.0/16')
ipNetwork = ipInterface.network
print(ipNetwork) #network address

college = list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff = 4))
print('The address of the first network, Applied Science, is',college[0])
print('The address of the second network, Arts & Humanities, is',college[1])
print('The address of the third network, Education, is',college[2])
print('The address of the fourth network, Business & Economics, is',college[3])
print('The address of the fifth network, Health, is',college[4])
print('The address of the sixth network, Science, is',college[5])
print('The address of the seventh network, Social & Behaviorial Science, is',college[6])
print('The address of the eigth network, Information Technology, is',college[7])
print('The address of the ninth network, Student Affairs, is',college[8])
print('The address of the tenth network, Facilities Management, is',college[9])
print('The address of the eleventh network, Administrative Services, is',college[10])

ipInterface = ipaddress.ip_interface(college[0])
ipNetwork = ipInterface.network
print('Applied Science', ipNetwork)
AppliedScience = list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff = 3))
print('The address of the first network, Computer Science, is',AppliedScience[0])
print('The address of the first network, Professional Sales, is',AppliedScience[1])
print('The address of the first network, Manufacturing Engineering, is',AppliedScience[2])
print('The address of the first network, Construction Management, is',AppliedScience[3])
print('The address of the first network, Automotive Technology, is',AppliedScience[4])
print('The address of the first network, Network Technology, is',AppliedScience[5])
print('The address of the first network, Web Design, is',AppliedScience[6])
print('The address of the first network, Engineering, is',AppliedScience[7])

ipInterface = ipaddress.ip_interface(college[1])
ipNetwork = ipInterface.network
print('Arts & Humanities', ipNetwork)
ArtsHumanities = list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff = 3))
print('The address of the first network, Korean, is',ArtsHumanities[0])
print('The address of the first network, German, is',ArtsHumanities[1])
print('The address of the first network, Spanish, is',ArtsHumanities[2])
print('The address of the first network, French, is',ArtsHumanities[3])
print('The address of the first network, English, is',ArtsHumanities[4])
print('The address of the first network, Visual Arts, is',ArtsHumanities[5])
print('The address of the first network, Performing Arts, is',ArtsHumanities[6])
print('The address of the first network, Communications, is',ArtsHumanities[7])

ipInterface = ipaddress.ip_interface(college[2])
ipNetwork = ipInterface.network
print('Education', ipNetwork)
Education = list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff = 3))
print('The address of the first network, Child & Family Studies, is',Education[0])
print('The address of the first network, Health Promotion, is',Education[1])
print('The address of the first network, Athletic Training, is',Education[2])
print('The address of the first network, Human Performance, is',Education[3])
print('The address of the first network, Teacher Education, is',Education[4])
print('The address of the first network, Exercise Physiology, is',Education[5])
print('The address of the first network, Health Education, is',Education[6])
print('The address of the first network, Recreation Management, is',Education[7])

ipInterface = ipaddress.ip_interface(college[3])
ipNetwork = ipInterface.network
print('Businees & Economics', ipNetwork)
BusinessEconomics = list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff = 3))
print('The address of the first network, Business Administration, is',BusinessEconomics[0])
print('The address of the first network, Economics, is',BusinessEconomics[1])
print('The address of the first network, Information Systems Tech, is',BusinessEconomics[2])
print('The address of the first network, Master of Bus Admin, is',BusinessEconomics[3])
print('The address of the first network, Accounting, is',BusinessEconomics[4])
print('The address of the first network, Business Education, is',BusinessEconomics[5])
print('The address of the first network, Master of Accountancy, is',BusinessEconomics[6])
print('The address of the first network, Master of Taxation, is',BusinessEconomics[7])

ipInterface = ipaddress.ip_interface(college[4])
ipNetwork = ipInterface.network
print('Health', ipNetwork)
Health = list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff = 3))
print('The address of the first network, Dental Hygiene, is',Health[0])
print('The address of the first network, Emergency Care, is',Health[1])
print('The address of the first network, Health Information Mngt, is',Health[2])
print('The address of the first network, Nursing, is',Health[3])
print('The address of the first network, Medical Laboratory, is',Health[4])
print('The address of the first network, Radiology, is',Health[5])
print('The address of the first network, Respirtory Therapy, is',Health[6])
print('The address of the first network, Occupational Therapy, is',Health[7])

ipInterface = ipaddress.ip_interface(college[5])
ipNetwork = ipInterface.network
print('Science', ipNetwork)
Science = list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff = 3))
print('The address of the first network, Botany, is',Science[0])
print('The address of the first network, Geosciences, is',Science[1])
print('The address of the first network, Microbiology, is',Science[2])
print('The address of the first network, Developmental Math, is',Science[3])
print('The address of the first network, Physics, is',Science[4])
print('The address of the first network, Zoology, is',Science[5])
print('The address of the first network, Mathematics, is',Science[6])
print('The address of the first network, Human Anatomy & Physiology, is',Science[7])

ipInterface = ipaddress.ip_interface(college[6])
ipNetwork = ipInterface.network
print('Social & Behavioral Science', ipNetwork)
SocailBehavioralScience = list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff = 3))
print('The address of the first network, Criminal Justice, is',SocailBehavioralScience[0])
print('The address of the first network, Geography, is',SocailBehavioralScience[1])
print('The address of the first network, History, is',SocailBehavioralScience[2])
print('The address of the first network, Military Science, is',SocailBehavioralScience[3])
print('The address of the first network, Phylosophy and Poli Sci, is',SocailBehavioralScience[4])
print('The address of the first network, Psychology, is',SocailBehavioralScience[5])
print('The address of the first network, Social Work, is',SocailBehavioralScience[6])
print('The address of the first network, Socialogy & Anthropology, is',SocailBehavioralScience[7])

ipInterface = ipaddress.ip_interface(college[7])
ipNetwork = ipInterface.network
print('Information Technology', ipNetwork)
InformationTechnology = list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff = 3))
print('The address of the first network, Computing Support, is',InformationTechnology [0])
print('The address of the first network, Telecommunications, is',InformationTechnology [1])
print('The address of the first network, Administrative Computing, is',InformationTechnology [2])
print('The address of the first network, Networking, is',InformationTechnology [3])
print('The address of the first network, Academic Computing, is',InformationTechnology [4])
print('The address of the first network, Computer Security, is',InformationTechnology [5])
print('The address of the first network, Database Administration, is',InformationTechnology [6])
print('The address of the first network, VP of IT Office, is',InformationTechnology [7])

ipInterface = ipaddress.ip_interface(college[8])
ipNetwork = ipInterface.network
print('Student Affairs', ipNetwork)
StudentAffairs = list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff = 3))
print('The address of the first network, Student Life, is',StudentAffairs[0])
print('The address of the first network, Student Services, is',StudentAffairs[1])
print('The address of the first network, Outreach, is',StudentAffairs[2])
print('The address of the first network, Academic Support, is',StudentAffairs[3])
print('The address of the first network, Focused Interest, is',StudentAffairs[4])
print('The address of the first network, Career Services, is',StudentAffairs[5])
print('The address of the first network, Veterans Affairs, is',StudentAffairs[6])
print('The address of the first network, Diversity, is',StudentAffairs[7])

ipInterface = ipaddress.ip_interface(college[9])
ipNetwork = ipInterface.network
print('Facilities Management', ipNetwork)
FacilitiesManagement = list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff = 3))
print('The address of the first network, Campus planning, is',FacilitiesManagement[0])
print('The address of the first network, Construction, is',FacilitiesManagement[1])
print('The address of the first network, Custodial, is',FacilitiesManagement[2])
print('The address of the first network, Landscaping, is',FacilitiesManagement[3])
print('The address of the first network, Electrical, is',FacilitiesManagement[4])
print('The address of the first network, Mechanical, is',FacilitiesManagement[5])
print('The address of the first network, Business Services, is',FacilitiesManagement[6])
print('The address of the first network, Parking Services, is',FacilitiesManagement[7])

ipInterface = ipaddress.ip_interface(college[10])
ipNetwork = ipInterface.network
print('Administrative Services', ipNetwork)
AdministrativeServices = list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff = 3))
print('The address of the first network, Athletics, is',AdministrativeServices[0])
print('The address of the first network, Accounting, is',AdministrativeServices[1])
print('The address of the first network, Budget, is',AdministrativeServices[2])
print('The address of the first network, Enviro Health & Safety, is',AdministrativeServices[3])
print('The address of the first network, Printing, is',AdministrativeServices[4])
print('The address of the first network, Human Resources, is',AdministrativeServices[5])
print('The address of the first network, Purchasing, is',AdministrativeServices[6])
print('The address of the first network, Police & Security, is',AdministrativeServices[7])