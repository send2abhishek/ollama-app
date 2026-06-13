## Vajra Onboarding User Guide

- Introduction to Vajra
- Phases in Vajra
- Onboarding the system
- -Why System Onboarding
- -Vajra URL For Onboarding
- -Login Restriction
- -Tech Stack Supported
-  Ways Of Onboarding
- Azure SQL Onboarding
- Akeyless and secrets Injection
- Uploading JKS files as secrets
- Mocking or Stubbing the Request
- Onboarding Secure Kafka To Vajra
- Designing a Pipeline
- Building a Pipeline
- Deploying a Pipeline in K8
- Component Bulk Update Based On Pipeline
- Namespace Request
- Access Restriction
- Quota Requirements
- Kubernetes Cluster Access
- Deployment Expiry
- External TCP Option
- MPS kafka Connectors
- For Support
- CronJob Onboarding

## Introduction to Vajra

Vajra is a platform which provides an on-demand sandbox environment for application owner/teams to do their functional testing of components as well as Integration testing/E-E system testing.It also helps developer to quickly check the impact of their latest code changes in isolated/sandBox environment as part of CICD flow .

## Phases In vajra

Every system which will get deployed in sandbox environment of K8 through vajra platform has to pass through below phases .

## On Board

During on-boarding process app owner has to provide all the system related info to the vajra platform in order to create docker image out of it .

## Mocking/Stub

If you don't want to onboard the system or whitelist it then we have the option of stubbing the component. This is optional but if you want to include any mocking please create it before design phase .So that it        can be included in the pipeline design before pipeline build &amp; deployment .

## Design Pipeline

In this phase user can design the replica of their system architecture by connecting all the required onboarded components. It depends on the On-boarding phase as user has to complete all the onboarding of required components for designing a pipeline. After designing user has to SAVE the pipeline for next phase(Pipeline Build) .

## Pipeline Build

Once the Pipeline is SAVED in the design phase . We need to trigger a build for the saved pipeline . Once the pipeline build is ready , user can deploy that build .

## Deploy

4 VAJRA Login

In this phase user deploy the certified build in vajra sandbox environment i.e Kubernetes(K8) .

## Testing

If deployment is SUCCESS or all the pods of deployed pipeline comes up . User/ Team can do functional / integration testing as part of CICD flow .

Domain

Homeoffice

## Onboarding the System

In vajra - onboarding means application owner will come up with their system related information and then through Vajra they can create docker images of all the system involved in the architecture automatically.

## Why System Onboarding

Vajra deploys the designed pipeline / replica of system architecture in Kubernetes and we know Kubernetes understands only container. So Vajra also uses Docker as container runtime environment for K8 and allows users to containerise their applications. So basically onboarding means containerise your apps for deploying in kubernetes namespace by providing system related information to vajra platform .

## Vajra URL For Onboarding

To onboard the system in vajra please use below url :- https://vajra.walmart.com

## Login Restriction

For login into vajra , users needs to contact slack channel for creating account into vajra &amp; other login related queries. Vajra also #vajra-onboarding provide role based access for component Onboarding , Pipeline designing &amp; deployment . Currently we support Admin, Design &amp; Deploy user access based on roles.

After user login account created in vajra . You can provide below information in login screen to get access . UserName &amp; Password is your's Walmart credential , Vajra don't store user password as it uses Walmart's IAM API to authenticate directly .

<!-- image -->

## Tech Stack Supported

- TOMCAT &amp; SPRINGBOOT as Services .
- KAFKA &amp; CASSANDRA as DataSource.
- STORM as Platform.
- MONGODB, COUCHBASE , SOLR , DEFAULT (Any Docker Image) as Docker.
- MOCKING through Vajra Stub server which internally uses wiremock server API along with vajra stub APIs.

## Ways Of Onboarding

There are 2 options through which user can onboard systems into vajra platform.

1.

VAJRA

Search Menu

On Board

Stub List

Pipeline List

Build List

Component

Ora Name *

catdev

1. Onboarding through one Ops Configuration - Supported only for TOMCAT &amp; SPRINGBOOT application .
2. Onboarding through Manual Configuration .

PartnerDataReceiver

Platform Name *

Caution : Please be aware that the HTTPS, HTTP &amp; TCP Whitelist DNS mentioned in the component onboarding will be whitelisted from the sandbox environment of the vajra and components will be able to access it when you run it in Kubernetes environment.

prod

## Onboarding through one Ops configuration  :-

Deployment List

## Applicable for Tomcat &amp; SpringBoot only .

Collapse

Name: catalog-stg

TOMCAT

com.walmart.cat

If the user has already one ops assembly then vajra tool can get details from the design and fill in all the information that is needed to dockerize the system. Currently, this will work only for the &amp; design. Please enter the one ops design information like Org Name, Assembly Tomcat SPRINGBOOT Name, Platform Name, Environment and click fetch "From One Ops button". Vajra tool will get all details from the One Ops and fill in the onboard form for you. Name: Gatekeeper TOMCAT com.walmart.ser

Description: gatekeeper

For this importing to work we need access to your org. Please provide access to "svcvajra" user in your org before you import the assembly.

Description: gatekeeper-sync

Name: iqs-stg

Description: IQS Stage

<!-- image -->

## Onboarding through Manual Configuration :-

Applicable for all the Components Like Tomcat , SpringBoot , Cassandra , Kafka , Storm &amp; Docker .

1.  Tomcat Or SpringBoot Manual Onboarding Steps :-

Click on 'On Board' present on left side of screen  Click on 'SERVICES' tab  Click on 'MANUAL' button  Select 'Services' as 'Category' &amp; 'tomcat /springboot' as 'System' in the right panel .

On Board

TOMCAT

com.walmart.ser

VAJRA

VAJRA

Search Menu

Search Menu

On Board

On Board

Stub List

©

Stub List

Design Pipeline

&amp;. Design Pipeline

Pipeline List

Pipeline List

Build List

Build List

Deployment List

Deployment List

Collapse

On Board

On Board

MANUAL

ONE OPS

MANUAL

ONE OPS

<!-- image -->

Collapse

- # Below is the Tomcat onboarding form. Springboot have similar form to Onboard .

<!-- image -->

Component

Component

Category

Services

• Auto Sync

Name *

tomcat

Description *

springboot

Artifacts

Nexus Repository *

pangaea\_releases

- # Input Fields required to do Manual Tomcat / Springboot Onboarding :-

| Fields                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Auto-Sync              | Enabling of this check box is required if you want to sync your onboarded component later point of time with nexus repository                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Name                   | Name of your system . Vajra accepts unique name . So better to add your component env suffix after the name, eg- Partner-data-reciever- prod                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Description            | Description of the component and the system that is represents                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Hostname               | The Hostname of the system , example- partner.dataingestor.prod.walmart.com                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| System                 | It's combination of tomcat, Jdk & Os version, on which your system will run                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Context path           | It's web app's context path, example- partner-data-ingestor-app                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Port                   | Port on which the tomcat service is exposed .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Memory required        | The minimum amount of RAM required for the system to start and take up a few requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Health Check End Point | It's web app's health check end-point , example - /deepCheck                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Health Check Header    | Headers required to hit health check end point.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Java Opts              | The JAVA_OPTS needed for your application in tomcat                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Dependen cies          | If your system is dependent on another system which is a READ only system then you can mention the hostname of that system in this field.Hostnames that are mentioned here will be whitelisted and will be allowed by the vajra network to contact the actual system in Walmart network. Currently vajra supports HTTPS, HTTP & TCP as Dependencies host . Note: It is not recommended that you include any production hosts in your dependencies whitelist. Please note that if you add any prod host to the dependencies, it will make calls to your prod services and pollute the prod data. |
| Artifacts              | It's nexus repository details like Nexus Repository, Group Id, ArtifactId, Extension & Classifier (Optional). Example is shown below .                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Env Variable           | Environment variables that need to be set in the system during the deployment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

Group Id *

Artifactld*

1.72.PROD

Extension *

war

Classifier (optional)

Classpath

CCM Sandbox

CCM Application Name repository

partner-data-ingestor-app pangaea\_releases

CCM Environment|

groupld com.walmart.partnerapi

prod artifactld

gateway-error-store artifactVersion

1.0.23.81

classifier extension

jar

<!-- image -->

CCM Download Online Y

Attachments

Destination Path

<!-- image -->

After the Onboarding process is complete , we can click on the 'SERVICES' tab to list down all the onboarded components along with other details like Created\_by, Created\_On etc . There is drop down list to the onboarded component along with features . ACTION view, edit, delete CLONE &amp; SYNC

## CLONE

This feature will allow you to clone a component on just a button click . Example suppose you want to do some changes in the onboarded component but if you do it in existing one it can impact running pipeline. So better first clone it and then do the modification . After that you can add it to the pipeline design for your testing . Currently clone feature is applicable for TOMCAT, SPRINGBOOT, STORM, and DOCKER components.

## SYNC

This feature will allow you to do sync of your onboarded component with nexus repository . Example suppose some team has pushed new jar/war file to nexus for your onboarded component but your pipeline is still using the old one . So in this case you can sync all the components or the required components involved in the pipeline design and can upgrade the pipeline with all the latest war .

## 2.  Kafka Manual Onboard Steps :-

Click on 'On Board' present on left side of screen  Click on 'DATASOURCE' tab  Click on 'MANUAL' button  Select 'Data source' as 'Category' &amp; 'kafka' as 'System' in the right panel .

Note: If you deploy any data sources like Kafka and Cassandra in WCNP cluster for an extended period of time, it may result in problems down the road after a few days in the pipeline because the maximum disc space permitted in containers is 1GB.

VAJRA

VAJRA

Search Menu

On Board

On Board

MANUAL

Stub List

Design Pipeline

Pipeline List

Build List

Deployment List

‹ Collapse

On Board

MANUAL

ONE OPS

System

-

kafka

—kafka

-

<!-- image -->

#Below is the Kafka onboarding form .

<!-- image -->

#Input fields required to do Manual kafka onboarding .

| Fields      | Description                                                                                                                     |
|-------------|---------------------------------------------------------------------------------------------------------------------------------|
| Name        | Kafka system name. It is better to attach for which environment you are configuring the component, Eg. feed-gateway-kafka-stage |
| Description | Description of the component and the system that is represents                                                                  |

ONE OPS

Component

Component

Category

Category

Data source

Data source

Kafka

4 VAJRA

Search Menu

On Board

Stub List

El Pipeline List

Build List

On Board

Component

Cassandra

Import Schema

| Version        | Kafka version                                                                          |
|----------------|----------------------------------------------------------------------------------------|
| Broker List    | List of broker hostnames as comma-separated values                                     |
| Topic List     | List of topics to be created. Note: Auto topic creation is enabled by default in vajra |
| Consumer group | List of consumer groups to be created                                                  |

Deployment List

Description: uber-cassandra

Name: catalog-kafka

Description: kafka for catalog service.

Collapse

## 3. Cassandra Manual Onboarding Steps :-

KAFKA

KAFKA

Click on 'On Board' present on left side of screen  Click on 'DATASOURCE' tab  Click on 'MANUAL' button  Select 'Data source' as 'Category' &amp; 'cassandra' as 'System' in the right panel . KAFKA

Description: bigben kafka

Please refer step 2 above for screen shot .

Description: offer store cassandra

Note: If you deploy any data sources like Kafka and Cassandra in WCNP cluster for an extended period of time, it may result in problems down the road after a few days in the pipeline because the maximum disc space permitted in containers is 1GB.

Name: item-asset-blobstore-cassandra-sync

Description: blob store cassandra for item asset

#Below is the Cassandra onboarding form .

CASSANDRA

CASSANDRA

Data File (optional) ®

<!-- image -->

#Input fields required to do Manual Cassandra onboarding .

| Fields       | Description                                                                                                                              |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Auto Sync    | Enabling is required for syncing the Cassandra component with latest schema file .                                                       |
| Name         | Cassandra system name. It is better to attach for which environment you are configuring the component, Eg. feed-gateway-cassandra- stage |
| Description  | Description of the component and the system that is represents                                                                           |
| Version      | Cassandra version. Currently supported version is 2.1.20 & 3.11                                                                          |
| Cluster name | Cassandra cluster name (e.g. hyperloop)                                                                                                  |

&lt;

CASSANDRA

Cluster Hosts *

VAJRA

Search Menu

On Board

Stub List

&amp;. Design Pipeline

El Pipeline List

Build List

Collapse

## SYNC

On Board

MANUAL

Component

Category

Platform storm

| Read only username   | Username & Password of cassandra cluster is required to import the schema or Syncing the schema from cluster automatically .                                                                                                                      |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Read only password   | Username & Password of cassandra cluster is required to import the schema or Syncing the schema from cluster automatically .                                                                                                                      |
| Cluster hosts        | List of cluster hosts as comma-separated values. It can either ip address or domain names.                                                                                                                                                        |
| Schema file          | Upload .cql file representing the schema. It is recommended to use the "Import Schema" button shown above in the snapshot to download the schema file. Make sure the script has only one datacenter "cdc" and network policy as "simple strategy" |
| Data file            | If the system needs a master data then CQL file with data can be uploaded here.                                                                                                                                                                   |

r-prod-topology

ONE OPS

STORM

com.walmart.storm : product-pipeline: 0

com.walmart.storm : product-pipeline: d

After the datasource (cassandra &amp; kafka) onboarding process complete, We can click on the 'DATASOURCE' tab to list down all the onboarded components along with other details like Created\_by, Created\_On etc . There is also drop down list to the onboarded ACTION view, edit, delete component along with feature for cassandra . SYNC

sipeline-stage-topology STORM

iset pipeline stage topol validator

STORM

com.walmart.storm : product-pipeline: d com.walmart.qarth : walmart-spec-parse

This cassandra SYNC feature will be helpful in upgrading the cassandra schema automatically . But it requires correct username &amp; password to connect cassandra cluster to get latest schema .

4. Storm Manual Onboarding Steps :-

Click on 'On Board' present on left side of screen  Click on 'PLATFORM' tab  Click on 'MANUAL' button  Select 'Platform' as 'Category' &amp; 'storm' as 'System' in the right panel .

<!-- image -->

#Storm onboarding form for Manual onboarding :- egular topology, part of

&lt;

VAJRA

Search Menu

On Board

Stub List

©

Design Pipeline

=ll Pipeline List

Build List

Deployment List

Collapse

On Board

MANUAL

ONE OPS

<!-- image -->

#Input fields required to do Manual Storm onboarding .

| Fields        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name          | Storm topology name. It is better to attach for which environment you are configuring the component, Eg. spec-parser-validator-stage                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Descript ion  | Description of the component and the system that is represents                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Version       | Storm cluster version in which the topology has to be submitted                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Run params    | The run parameters that need to pass to the submitting topology                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Main class    | Submitting topology's main class                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Artifacts     | It's nexus repository details like Nexus Repository, Group Id, ArtifactId, Extension & Classifier (Optional).                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Depend encies | If your system is dependent on another system which is a READ only system then you can mention the hostname of that system in this field.H ostnames that are mentioned here will be whitelisted and will be allowed by the vajra network to contact the actual system in Walmart network. Currently vajra supports HTTPS, HTTP & TCP as Dependencies host . NOTE : - Dependencies fields will be in tomcat, springboot, storm & docker . Note: It is not recommended that you include any production hosts in your dependencies whitelist. Please note that if you add any |
| Classpa th    | Add all the files that need to be placed in the classpath of the running topology                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## 5. MongoDB, CouchbaseDB, Solr Manual Onboarding Steps :-

Click on 'On Board' present on left side of screen  Click on 'DOCKER' tab  Click on 'MANUAL' button  Select 'Docker' as 'Platform' &amp; 'mongodb' | 'couchbase' | 'solr' as 'Template' in the right panel .

Component

Category

Platform

Storm Topology

System storm

4 VAJRA

VAJRA

On Board

On Board

MANUAL

MANUAL

SERVICES (548)

Component lame: wakanda-mbaku-core-snapshot

Jescription: Wakanda mbaku core snapshot test lame: SpecExcelGenerator

Jescription: SpecExcelGenerator lame: clone-124-limo-ingestion-stg

lescription: Limo Item Catalog Stage lame: clone-124-gatekeeper-sync-v2

escription: gatekeeper-sync-v2

Jescription: yugabyte lame: clone-124-variant-grouping-stream-prod

Jescription: prod mongodb for classificationn lame: clone-124-pt-gpt-classification

)escription: product type classification

Jescription: Source Normalization WCNP Prod

Total Count • 547 Pace.

Component

Category

Docker mongodb

Component

Category

Docker

Mongodb

<!-- image -->

Please note we have pre-build images for mongo, couchbase &amp; solr Db in vajra .  That's why in below snapshot most of the fields values are pre-populated and remaining user has to enter in order to complete the onboarding for those Db.

## #Supported DB Manual Onboarding form .

NOTE:-  Since all have same temple . Hence showing example for one (mongoDb).

<!-- image -->

#Input fields required to do Manual Db onboarding .

| Fields      | Description                                 |
|-------------|---------------------------------------------|
| Name        | Name of the System/Db                       |
| Description | Description of the system that it represent |

4

ONE OPS

ONE OPS

Template mongodb

Env Variable

Akeyless Secrets key

MONGO\_INITDE\_DATABASE

key test-ad-group

key

MONGO\_NON\_ROOT\_USERNAME

key key

<!-- image -->

value

Akeyless Secrets srcSecretPath

Files secretName

app secretName

dev

<!-- image -->

## 6. Docker image Manual Onboarding Steps :-

Click on 'On Board' present on left side of screen  Click on 'DOCKER' tab  Click on 'MANUAL' button  Select 'Docker' as 'Platform' &amp; then select either of the below template

- 'Default' - When you have the docker image and just want to deploy it with the basic functionalities.
- 'Service' - When the docker image you want to onboard is an application/service and want to use additional features like healthCheckEndPoint and CCM config overriding.

For screenshot, please refer above Docker section.

Vajra support onboarding of already build docker image of application . With this we can pass through manual onboarding of system by providing very minimum details in onboarding form .

# Docker Image manual onboarding form :-

4 VAJRA

Env Variable

On Board key

MANUAL

ONE OPS

JAVA\_OPTS

SERVICES (661)

key

Select

Total Count: 661 Page:

value

<!-- image -->

Template is same as Db onboarding shown above except few fields mentioned below . For other fields details please refer above table.

<!-- image -->

| Fields                 | Description                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                             |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name                   | Name with which you need to onboard the docker component                                                                                                                                                                                                                                                | Name with which you need to onboard the docker component                                                                                                                                                                                                                                                |
| Image Name             | Image path to download from nexus. E.g - docker.prod.walmart.com/catalog-services/uber-slap-akka-stream                                                                                                                                                                                                 | Image path to download from nexus. E.g - docker.prod.walmart.com/catalog-services/uber-slap-akka-stream                                                                                                                                                                                                 |
| Host                   | The Hostname of the system , example- partner.dataingestor.prod.walmart.com                                                                                                                                                                                                                             | The Hostname of the system , example- partner.dataingestor.prod.walmart.com                                                                                                                                                                                                                             |
| Tag                    | Version of the image to be downloaded .                                                                                                                                                                                                                                                                 | Version of the image to be downloaded .                                                                                                                                                                                                                                                                 |
| Exposed Port List      | Port number exposed by application for accessing it from outside .                                                                                                                                                                                                                                      | Port number exposed by application for accessing it from outside .                                                                                                                                                                                                                                      |
| Mount Path             | Currently this field is not getting used but since made mandatory in UI . Please enter some path like /data/schema. We will remove it .                                                                                                                                                                 | Currently this field is not getting used but since made mandatory in UI . Please enter some path like /data/schema. We will remove it .                                                                                                                                                                 |
| Health Check End Point | It's web app's health check end-point , example - /deepCheck                                                                                                                                                                                                                                            | It's web app's health check end-point , example - /deepCheck                                                                                                                                                                                                                                            |
| Runtime params         | The run time params if any needed for running the Db                                                                                                                                                                                                                                                    | The run time params if any needed for running the Db                                                                                                                                                                                                                                                    |
| Dependen cies          | Host name / DNS of any other dependent system . This is optional . Note: It is not recommended that you include any production hosts in your dependencies whitelist. Please note that if you add any prod host to the dependencies, it will make calls to your prod services and pollute the prod data. | Host name / DNS of any other dependent system . This is optional . Note: It is not recommended that you include any production hosts in your dependencies whitelist. Please note that if you add any prod host to the dependencies, it will make calls to your prod services and pollute the prod data. |
| Env variable           | Environment variables that need to be set in the system for running the Db .                                                                                                                                                                                                                            | Environment variables that need to be set in the system for running the Db .                                                                                                                                                                                                                            |
| Env variable           |                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                         |
| Env variable           |                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                         |

Component

Category

Docker

Service

Template service

Init Files &amp; Path

Secrets key|

srcSecretPath key

destSecretPath

Init File Path

/tmp/

value

<!-- image -->

CCM Config

Override

Sandbox

## CCM Config

CCM Application Name uber-product-service

CCM Environment|

prod/scus

Sandbox Override

If you are system is using CCM and if you want to override any of the properties specifically for integration testing please mentioned it in this section.

CCM Application Name, CCM Environment and overridden properties file as a ZIP format. Please note all the files has to be selected together and then zip it for upload.

There are three options displayed for configuring CCM properties.

- override: if you want to override any of the properties specifically for integration testing.
- sandbox: sandbox allow you to put all the CCM configuration locally inside the K8 container instead of reading any configurations from CCM server.
- sandbox override: a combination of both override and sandbox.

Please note that for docker onboarding, vajra currently supports only override feature, so please choose override during ccm configuration.

And you can have more than one CCM uploads as part of your system requirement in vajra . Example shown below .

<!-- image -->

NOTE :- Zip download options will be available in component edit mode . You can download your uploaded zip file locally for review &amp; editing. Same is applicable for Init Files &amp; Path section.

key

Override ccm.city

key key

ccm.envName key

ccm.serviceld key

ccm.envProfile key

ccm.configs.dir key

ccm.polling.enabled key

jsse.enableSNIExtension cem. serviceConfis Version

Sandbox Sandbox Override

CCM2|

CCM2 Agent

<!-- image -->

## Azure SQL Onboarding

To onboard azure sql instances onto vajra, you can refer to the existing docker component "azure-sql". This component can be cloned and used. This is azure sql docker image provided by vajra itself. Users are required to provide schema and seed data files alone in the component under Init Files section.

On Board Component

Category

Docker

Default autoSync *

Name *

azure-sql

Stage non-prod

Image Name *

1433

AD Groups *

vajra

Env Variable

Akeyless Secrets

Resource Limit

Init Files &amp; Path

<!-- image -->

Template

-GATEWAY

Init Files &amp; Path

E AKEYNESS

Init File Path tmp/

Init File Path

/tmp/

<!-- image -->

## Akeyless and secrets Injection:

Several applications have secrets and would want those secrets to be injected into the pod at a particular path. Hence, Vajra leverages a platform called akeyless to store secrets inject them into vajra pods during deployment. . Once they do, Users can reach out to Vajra team for AD access to Akeyless they must be able to create their secrets inside the root directory . 'Non-Prod/vajra/&lt;your-AD-folderName&gt;/'

Please follow the detail steps on how to access akeyless and creating secrets given below.

- Please raise a JIRA request to get access to Vajra akeyless. Users can raise access request here
- Login to akeyless portal using your LDAP credentials.
- User will now be able to see his AD-folderName created for the team, once they log in.

<!-- image -->

AKEYLESS

- WMT

** Global Tech

07 Secrets &amp; Keys

+Pin Tag

&amp; Access Roles

Auth Methods

(:)) Gateways

Data Protection

Il. Analytics

Integration Center

© Online Support

Documentation

0r Secrets &amp; Keys

= Switch to List View

<!-- image -->

- The team can then create their secrets inside that particular folder. Only users who are part of that AD group will be able to view/edit/delete secrets inside that folder.

During deployment we inject those secrets as a file inside the pod. To ease the load on users to provide file extensions for each secrets while NOTE: onboarding on Vajra, it is expected from users that when you create secrets in akeyless, please provide the file extension as well in the secrets . We will be using the secret name as the fileName while injecting secrets into the pods. For eg, if the secret name is 'testSecret' and in path they name want to save it as 'testSecret.properties', please save the secret as 'testSecret.properties' in akeyless. Please refer the below example for the same.

C

* New

(•2)

AKEYLESS

WMT

** Global Tech

Or Secrets &amp; Keys

+Pin Tag

Access Roles

Auth Methods

Gateways

Data Protection

Il. Analytics

• Integration Center

Online Support

Documentation

<!-- image -->

## Onboarding Secure Kafka To Vajra

Some applications might be using secure kafka(port-9093) in their applications. Kafka instance provided by Vajra is 9092. Follow these simple steps while on boarding your kafka component in vajra.

1. change port 9093 to 9092. (Override this port in ccm or wherever its configured for your application to connect.)
2. security.protocol to PLAINTEXT from SASL\_SSL (Override this config as well wherever its configured)
3. disable ssl from the configs (Override this config as well wherever its configured)

## UPLOADING JKS FILES IN AKEYLESS:

Currently, Vajra only supports static secrets to be injected during pod deployments. Hence, it is not possible to directly upload the jks files. Even copying the content of jks file as a secret value would corrupt it. To upload a jks file as a secret, please follow the following steps.

- Encode the jks file in your system using Base64. For example, if the fileName is 'truststore.jks', then run the following command (macOS) in your terminal to encode it. The below command will encode the jks file and save it into a new text file
- Once the file is encoded, copy the contents of the text file
- Create a static secret in Akeyless with the name '&lt;yourFileName&gt;'. For example, if the fileName is 'truststore.jks', then create a secret where secretName - truststore.jks

<!-- image -->

secretValue - copied contents of the encoded text file

- When Vajra injects the secrets into the path, it will automatically decode the secret and have it in place. Please refer the below for an example with a jks file as a secret.

or Secrets &amp; Keys

= Switch to List View

* New

AKEYLESS

WMT

** Global Tech

Secrets

Secrets

Or Secrets &amp; Keys key|

key

+Pin Tag

Users &amp; Auth Methods key

destSecretPath key

(1;2

destSecretPath

Gateways

Data Protection

Integration Center

Online Support

Documentation

07 Secrets &amp; Keys value

test-ad-group value

<!-- image -->

- Once secrets have been successfully created in akeyless, users must provide the secret path while onboarding the component.
- srcSecretPath: The name of the AD-folderName in which the secrets have been created by the team. For example, if in akeyless, the secrets have been created in the path '/Non-Prod/vajra/&lt;your-AD-folderName&gt;', then the srcSecretPath must be 'your-AD-folderName'. Add 'decode\_&lt;yourFileName&gt;' in the path to decode base64 encoding.
- destSecretPath: The path in the pod, where the secrets must be injected. For example, /etc/secrets

<!-- image -->

<!-- image -->

## Mocking Or Stubbing the Request

If you don't want to onboard the system or white list it then we have the option of stubbing the component. Please note currently we support STATIC &amp; TEMPLATE as response Type only. Internally we use Wiremock server APIs to mock the req/res , So please refer wiremock docs -  http://wiremock.org /docs/request-matching/ as reference guide for onboarding the stub in vajra platform .

Click on 'Stub List' present on left side of screen  Click on 'CREATE STUB' tab  Will open Stub onboarding form - shown below for reference

• New

Static Secret decode\_truststore.jks/

3.32.0

Update Available

4 VAJRA

VAJRA

Design Pipeline

Stub List

Search Components.

+O STENCIL

CREATE STUB

SERVICES

Stub ID

• PLATFORM |

• DOCKERS

• sTUBS

Stub

Dns"

• 10 Snaplines: M

inspectorM

Http Method

GET

Path*

ACTIONS -

Search within graph…

Pipeline Name: vajra-demo-16feb

Build Name:

Basic Auth Key

• Equal • Pattern Match |

Basic Auth Value

<!-- image -->

## Designing a Pipeline

After all the onboarding are completed we can start pipeline design phase where user will be designing the whole system architecture by connecting the onboarded components .

## OPTION\_1

1. Click on the "System Design" screen from the left menu.
2. Left panel section (called STENCIL) has list of the components on boarded and stubs
3. In the STENCIL section we have facility to search for components across all section like services, datasources, platform, Docker, stubs .
4. Drag and Drop the component in to the canvas in the middle section . User can also use/drag only the respective template and then search it on the right side panel for the component.
5. Connect the components based on the start up dependency .
6. Before saving the pipeline user can search for any components added through right corner search option during review / validation of designed pipeline .
7. Then go to NEXT and Save the pipeline design after reviewing all the pieces related to pipeline like WHITELIST, SERVICES, DATASOURCE, PLATFORM, STUBS in the SAVE page .
8. After saving the pipeline user have options to BUILD &amp; DEPLOY from that page itself or they can do it from Pipeline List / Build List Page .

<!-- image -->

©

Export SVG

Export PNG

S

Send To Front

Send To Bac

VAJRA

Search Menu

On Board

Stub List

Pipeline List

= Build List

Design Pipeline

Filter

* item-asset-read-ap...

## OPTION\_2 - RECOMMEND TO USE ABOVE OPTION  ONLY AS IT IS ONLY FOR UNDERSTANDING PURPOSE .

- reingestion-webapp….

Click on 'Design Pipeline' present on left side of screen  It will open design panel along with all the onboarded components and stubs in vajra  Drag and Drop the component in to the canvas in the middle section  Connect the components based on the start up dependency  CLICK on Next .

Deployment List

‹ Collapse

&amp; normalization-serv....

• nzservice

<!-- image -->

#Sample screenshot shown below is for designing a pipeline . In the example panel shown below we have following features like :-

- a. User can do filtering of their components from the list using the option . FILTER
- b. User can do as well while designing a pipeline to get a better view of it in case of bigger pipeline . Zoom-in/out
- c.  User can select components and drag it to the right panel for designing .
- d.  On dragged component user have two options for deleting the component &amp; for connecting to the target component . delete symbol arrow symbol

#Please note below points while designing :-

- a. During design phase right side drop down list will be disabled . ACTION
- b. Connecting between DATASOURCE to DATASOURCE, DATASOURCE to SERVICES, DATSOURCE to PLATFORM is invalid .
- c. At the bottom there are three isolated components which are not connected to anyone represent involved as part of pipeline . STUBS

ACTIONS -

Build

Deploy|

VAJRA

4

VAJRA

Search Menu

Search Menu

• On Board

On Board

{Ö, Stub List

Stub List

. Design Pipeline

Design Pipeline

El Pipeline List

Pipeline List

#. Build List

# Build List

N Deployment List

Deployment List

‹ Collapse

Design Pipeline

Design Pipeline

Pipeline Name gateway-pipeline

hzseryice

<!-- image -->

‹ Collapse

After designing of pipeline is completed  please click on NEXT button which will land you to pipeline SAVE page shown below  Please enter the name of the pipeline before saving .

On the same page user have two options also as discussed below :-

- a. User can click on tab to the dependencies (HTTPS, HTTP, TCP) which has been entered as part of component WHITELIST Select/Unselect onboarding. So here it will list all the dependencies but as per pipeline requirement user can select ALL or unselect any.
- b. Similarly there are TABS to list down the components involved in the pipeline like SERVICES, DATASOURCE, PLATFORM etc .

<!-- image -->

## Building a Pipeline

ACTIONS

ACTIONS -

Deploy: Item-Ingestion

Certified

PB-9451e266-96cb-4c90-bf90-2f1801dd83e1 :

After the designed pipeline is saved you can find all the saved pipeline in Pipeline List screen as shown below . There are &amp; Actions Build/Deploy drop down list, discussed in details below . Actions support below operations on designed/saved pipeline :Actions

- a. -  User can view their saved pipeline. View

Pipeline Build

- b. - User can edit their saved pipeline . Edit
- c. -  User can clone the existing pipeline and save it as new pipeline. You can modify this pipeline as needed. Clone
- d. -  User can delete the pipeline . Delete

Build/Deploy Actions support below operations on designed / saved pipeline :-

- a. -       User can trigger a build for the saved pipeline. Build

- b. -       User have option to trigger a force build as well . Force Build

- c. -        Once build is ready, you can deploy it to kubernetes from here. Enter namespace &amp; select Pipeline build, Cluster, Node Selectors Deploy from dropdown and then click on button. You can also check the Certified Build options to DEPLOY certify the build . Once the deployment is triggered vajra will give you concord log url to check the deployment related logs also .
- d. - It will show the build status of recent/latest build triggered . Latest Build Status
- e. -  If required user can sync their TOMCAT &amp; CASSANDRA components with this options . Sync
- f. - It will show the active deployment of all the builds for the pipeline Active Deployment List

<!-- image -->

Cluster List vajra-stg-k8-cluster

Node Selectors

REFRESH

CANCEL

DEPLOY

VAJRA

Build Status -PB-06e4ae75-9640-4c03-9832-bc1b064d2f39

Search Menu

Component Name

• On Board bigben

D Stub List hzservice-sync

Design Pipeline partner-data-ingestor-sync

I Pipeline List gatekeeper-sync

# Build List shelf-service-qarth

# Deployment List merge-service-qarth

Collapse validation-service-qarth

bv-service-qarth supply-item-prod

ptc-normalization-service-qarth catalog-service-qarth

item-pricing-ingestion image-classification-service-qarth

matching-service-qarth trade-item-prod

classification-service-qarth item-pricing-read

Pipeline List

Pipeline Name

CreatedBy

Created Time

Last Modify Time

Actions

Build-Deployment Actior|

<!-- image -->

After the build is triggered for a pipeline , We can get list of all the pipeline's build form On the Build List page there is Actions dropdown list Build List . provided for some useful features discussed below .

-  User can deploy the pipeline build from here as well . Inputs required to deploy already discussed above . Deploy

-   User can view the Pipeline Build status through this option . It's actually the health status of each components present in pipeline . Status

-   User can view the graphical representation of their pipeline build along with components build status in the graph . View

<!-- image -->

Status

• SUCCESSI

VAJRA

4 VAJRA

Search Menu

Deployment List

• On Board

©

© Stub List

i

Deploy Id

&amp;. Design Pipeline

El Pipeline List

Build List

F. Build List

N Deployment List

‹ Collapse

Build List

Build Name

Build Time

PipeLineName

Created By

Last Modify Time

Actions

Search..

Active

My Deployments

<!-- image -->

## Deploying a Pipeline in K8

Now we are in last stage of Pipeline lifecycle i.e deployment of build pipeline . As we already discussed above we can do deployment from either DEPLOY options present in dropdown list of 'Build lIst' Or dropdown list of 'Pipeline List' . Actions Build/Deploy Actions

The default expiry of deployments done through Vajra is . After two days, the deployment is deleted to clear up the resources. Although, NOTE: two days users can extend the expiry of the deployment if they want to keep the pipeline running for certain period of time. Please refer below the steps to extend the expiry.

Sample screenshot shown below . Which has also Actions dropdown list with some important features discussed below :-

As discussed, the default expiry of deployments done through Vajra is . To extend expiry, please navigate to Deployment List Extend Expiry two days Actions  Extend Expiry.

<!-- image -->

4 VAURA

Deployment List

Pipeline

Deployment Status -84897a5b-0923-45ef-af5d- cеca5f776965

Select Component Name

Status gatekeeper-sync

• SUCCESS

Actions

Timestamps

- It will show the deployment status of build pipeline including all the components involved like tomcat, springboot, cassandra, kafka, storm and Status docker. User can also restart any services (tomcat/springboot)  by selecting the checkbox present against the component .

Build Name: PB-4c80f077-230f-4|

Pipeline: item-ingestion

Build Name: PB-4c80f077-230f-4|

qarth-prod-kafka item-asset-app-qarth-sync

• SUCCESSI

• SUCCESS

Actions

Actions +

Last Modify Time: 2020-09-11T06:35:31.200+0000

Deploy Time: 2020-09-10T09:00:12.608+0000

Last Modify Time: 2020-09-10T09:00:12.608+0000

<!-- image -->

View - User can view all the deployment related properties like graphical representation of pipeline build , whitelisting and components involved in the deployment, build name, namespace, status etc .

Details -  It also same as view .

Delete   With delete feature user can delete the deployed pipeline from the sandbox env i.e K8.

Download - User can download values.yml file of deployed pipeline. It's the same file which Helm uses for deployment through concord in vajra native K8 cluster.

ConcordLog - User can also view the deployed pipeline concord log though this feature .

## Deployment Upgrade

Usecase :- Suppose user has to change the component details like change in artifact version of an application involved in the pipeline design without redeploying the whole pipeline .

Solution :- Change the component details like version and then do the build of pipeline to include latest component artifact into build and then click on Depl option of new build from page. Please note first two records of below screenshots, where ' ' oy Build List PB-3dbd94be-cbc4-4a19-a2d0-4941ecf85c56 was old build for ' ' pipeline and after version change of an application user has triggered new build ingestion-pipeline-sync for the  ' i ngestion- pipeline-- ' '. sync ' from the page and got new build as Pipeline List PB-c990a3fd-a057-4a82-afc2-9dc9bc6989a6

Now user click on option from Actions drop down list of Build List page for new build mentioned above . Enter all the required details like DEPLOY Namespace, Cluster List, Node Selectors and click on DEPLOY .

• Active • My Deployments

4 VAJRA

4 VAJRA

Build List

Build List

Build Name

Build Name

Build Time

PipeLineName

Created By

Last Modify Time

Actions

Actions

Build Time

PipeLineName

Created By

Last Modify Time

<!-- image -->

After Clicking on option as shown above user will get two options again i.e which will just deploy the changed component in the DEPLOY UPGRADE existing pipeline and which will first clean the existing pipeline and then deploy the whole pipeline with new build . CLEAN &amp; INSTALL

<!-- image -->

## Steps to check the logs for deployed pipeline :-

## TOMCAT | SPRINGBOOT LOGS:-

For checking the logs of tomcat, springboot you need to login into vajra cluster and then by kubectl log cmd you can check the application console logs Or if application is using LOGMON then enable it by configuring the proper datacenter to write to a logmon file.

## STORM LOGS :-

1. First replace the below URL with your namespace where sync-ingestion-pipeline is namespace &amp; prod.vajra.k8s.us.walmart.net is cluster DNS .

VAJRA

System Design http://mergedstorm-122.sync-ingestion-pipeline.prod.vajra.k8s.us.walmart.net/index.html Search Components... - 20% Grid size

STENCIL

2. From Topology Summary select any topology you want to check the logs .
3. From Worker Resources click on port link and it will give you below link

http://stormsupervisor122-1:8000/log?file=productPipeline\_catdev-7-1600274475%2F6701%2Fworker.log

4. In the above link replace :8080 with namespace and cluster DNS like below and then you will get appropriate worker node logs. http://stormsupervisor122-1.sync-ingestion-pipeline.prod.vajra.k8s.us.walmart.net/log?file=sourcePipeline\_catdev-4-1600274468%2F6700%2Fworker.log

DATA SOURCE

## KAFKA | CASSANDRA LOGS:-

Cassandra

Kafka

For datasource also first login into vajra cluster and then using kubectl log cmd you can view the container logs and also you can ssh into container through kubectl cmd .

Cosmos

NOTE: Please find below the most common kubectl commands to view container logs and interact with the container -  Kubectl Commands

Storm

## Component Bulk Update Based On Pipeline

In case users need to update the version/tag/artifact details of all the components(tomcat, spring boot, python, docker) of an existing pipeline in groups without actually updating them individually, the option available in pipeline design page (ActionsBulk Update) can be used. Bulk Update

<!-- image -->

on clicking "Bulk Update" option, a dialog box appears where a csv file containing the details(component-type, component-name, artifact-version/tag, artifact-id, group-id, extension, repository) of all the components will be downloaded.

•10|

Snaplines:

Inspector:

ACTIONS -

Build

Deploy

Bulk Update

1 will

i

BulkUploadCSV-...csv

AutoSave

OFF

Home

Insert

Draw

VAJRA

System Design

ACTIONS+

<!-- image -->

Page Layout

Calibri (Body)

Possible Data Loss

A1

COMPONENT-TYPE|COMPONENT-NAME

2 Docker allacket

5 Tomcat-Service

6 Springboot-Service

7 Python-Service

37

Ready

12

Formulas v A^

• Tell me

2b Wrap Text v

General

EE Insert v

5x Delete v

<!-- image -->

Now, the version details can be updated in that csv file referring to the component name and its type and the same should be uploaded back and click on confirm. In case any component need not be updated, either it can be left as it is or that particular row can be removed from the table (optional).

• Comments

Data

Review

View

&amp; Share

VAJRA

System Design

ACTIONS -

<!-- image -->

Once uploaded, a task will be created to track on this upload process, which can be checked from task tracker table. task details will be shown on ui upon submitting the file.

In the task tracker table, you can find if its success or failed. In case success, the updated component names is displayed in the description column along with the pipeline name.

In case of failure, the components updated so far in the process(till before the component for which update failed) is displayed in the description.

i

VAJRA

System Design

Search Components.

STENCIL

VAJRA

ACTIONS

Inspector:

Search wit

Pipeline Name: wakanda-vajra1-

<!-- image -->

Task ID

<!-- image -->

Task Name

## Namespace Request

It is required to register your namespace details with vajra to proceed with the deployment. There are two options available

1.To register your existing wcnp namespace details with vajra using 'RequestNamespace Option' following the instruction below.

- a. To request for a new namespace for deploying from vajra, Select settings options from onboarding page  Request Namespace. Once submitted, kindly let vajra team / vajra onboarding channel know to approve the request.

Description

Created By

Time Taken

Status

Export

SVG

Expor

PNG

Upgrade pipeline successfully with task ID - 149

Track

Loons

Ghosters

Created On

10

Snaplines:

*

Toggle device toolbar - 2 4 M

4 VAJRA

On Board

Deploy: brand-tool-ui-test

MANUAL

ONE OPS

Build Status: SUCCESS

SERVICES (655)|

Namespace List

Artifacts

Select Namespace List

+ Add New Namespace

® The selected cluster supports sandboxing

Select Search criteria

All

Search…

Certified Build

Meenakshi Ramasamy

Feedback

Need Sandboxing

Components

Disable Suffix

<!-- image -->

2.  Incase you dont have any wcnp namespaces available, for poc reasons, you can request Vajra team to provide namespace in vajra clusters. For this, you have to contact the vajra team.
3. Another option is to create a new namespace from dx console or the same can be done via vajra ui also using 'Add New Namespace' option available as shown below

<!-- image -->

## Access Restriction

1. Only selected user can login into vajra application. Please contact #vajra-onboarding slack channel for login related queries.
2. User will be able to modify the component/pipeline which they own. Other users components/pipelines they can't modify.
3. User can view any other user's components for their pipeline design.
4. In case you need to modify already existing pipeline owned by others you can "Clone" in the pipeline listing screen from the "Actions" and modify the design as needed and save it as new pipeline.

## Quota Requirements

Based on the pipeline design, number of pipelines and the number of users from your team wants to test and run the pipeline we can arrive at the compute requirement. This compute capacity cost will be borne by the team / cost centre.  The compute quota has to be made available in the azure cloud for integrating with our k8s cluster to use it. The step by step guide to avail this compute quota will be made available soon. As of now please contact #vajraonboarding channel for assistance.

## Kubernetes Cluster Access

3. Namespace level: Setting up expiry at namespace level will delete any deploymer

'User Groups'.

Home &gt; WCNP › Namespaces › vajra

Deploy: test-pip-1

vajra

Build Status: SUCCESS

Splunk Cluster

Details

Cost

Namespace *

Custom Metrics

# CLONE &amp; EXTEND DATE

/ EDIT

• Certified Build External TCP Console Log Need Sandboxing D Disable Suffix

Splunk Index

Temp Namespaces

Please contact #vajra-onboarding channel to get read only access to the kubernetes cluster in which you have deployed the pipeline. We can use this to connect to docker container running within your namespace and tail the logs of the container if needed. This can be used along with the vajra-cli too if needed. Splunk Index: wonp\_vajra O wus-dev-aks-vajra

Country: US

APM ID: APM0012758

User Groups: vajra\_mt.\_group

Temp Namespace Quota Limit (%): 30 © CALCULATE

DL Notification Email: dileep.gidwani@walmartlabs.com

Temp Namespace Custom Metrics: Disabled O

Pipeline Build

Node Selectors

## External TCP Option

Multi Deploy suffix mOrOdkI|

Environment

Expires By

Manage GSLB via DX Console: Disabled ©

Expiry Unit

When cassandra/kafka is deployed as part of the pipeline, it cannot be accessed externally i.e it is not exposed so that can be connected from any external sources. CPU (Cores) Memory (GiB) Tenant Group Sku Type ® Cluster ID Status C Actions

Functionally, this isn't a problem. the pipeline flow works as expected. But incase, you want to read or write data in the dbs, have to sh into the respective db containers and using cqlsh and kafka commands  it can be achieved.

But, dbs can be provided with an external dns similar to the services deployed in vajra. This is achieved through this external tcp option.

- This option is supported only with vajra single tenant clusters. Not supported by wcnp clusters.
- To use this option, contact vajr ateam via #vajra-onboarding channel requesting to enable external tcp option. Once provided, you can see a checkbox - 'External TCP' while deploying. check that and proceed with deployment. Upon deployment, you can get an external dns and port for the db as well.

## Deployment Expiry

Expiry refers to the time by which the deployment is deleted automatically. The expiry date and time can be viewed in the deployment page against your deployment under 'Build Expiry Date' column.

## Vajra Clusters (wus-dev-aks-vajra) :

- When deployed in vajra clusters, the default expiry is 1 day. So, after 1 day from the time of deployment, it is deleted.

## WCNP Cluster :

- To delete resources deployed in wcnp clusters, Vajra need to have access to the namespace used for deployment. This can be checked from dx dashboard (as shown in the reference image attached below) with respect to the namespace if vajra ad Group (' ') is part of console vajra\_grp 'User Groups'.
- If the mentioned ad group 'vajra\_grp' is not part of it, please add it.
- Once given permission for vajra to your namespace, please let the vajra team know with namespace details for which it has been set.
- Now, once its added users wcnp deployments can also be deleted automatically as it is set.
- Setting the expiry, there are 3 ways to do so (deploying from UI)
1. During Deployment: you get the option to set it in deployment window while trying to deploy. This is set for that particular deployment only.
2. Pipeline Level : It can also be set at pipeline level. To do so, edit Pipeline  click next  you can can see Deployment Expiry option. This applies to this pipeline whenever deployed. This can be overridden using above method while deploying.
3. Namespace level : Setting up expiry at namespace level will delete any deployment being deployed in this namespace.

<!-- image -->

<!-- image -->

• DELETE

&amp; MIGRATE WORKLOAD

Note: Priority is set as 1, 2, 3. Whatever is et during deployment is taken. Otherwise pipeline level set value (if any) will be taken. Otherwise namespace level set value (if any) is taken. Finally if nothing is set, default value 1 day is set.

- To set expiry in plugin, just set it as n(d/h). n number of days/hours. d days. hhours. To use this as well, for wcnp clusters vajra ad group should be part of User groups in for the specified namespace.

## MPS Kafka Connectors:

Teams using mps kafka connectors in their applications can make use of this mps docker component available with Vajra.

Follow these steps to onboard mps into your pipelines

1. Clone the docker component - 'mps-vajra'.
2. With the cloned one, Under Env Variable section  modify these values accordingly
- a. TOPICS - the topic from which mps will be consuming messages. Only one topic can be configured.
- b. GROUP\_ID - give any name
- c. HTTP\_API\_ENDPOINT - the http endpoint to which mps should push the message to.
- d. WORKER\_BOOTSTRAP\_SERVERS - kafka end point where the topic exists. incase of vajra deployed kafka, give the external dns and port details (kafka in vajra has to be deployed with external tcp option enabled). For actual kafka, broker details can be given.
- e. Don't change/modify/remove the other env variables available in the cloned component.
3. Under Env Variables section, you will find three configs named =&gt; WORKER\_CONFIGS\_TOPIC, WORKER\_OFFSET\_STORAGE\_TOPIC, WORKER\_STATUS\_STORAGE\_TOPIC having values compName-config, compName-offset and compName-status respectively. Rename them. it has to be unique for every mps component.
4. Once all the above steps are done, include the component in your pipeline and deploy them.
5. Once deployed and mps logs are loaded, you need to start it using the following end point.
- a. http://&lt;mps dns you get after deploying in vajra&gt;/connectors/start\_all
6. Now, you are ready to push the message in your kafka topic mentioned in mps configs which will be posted to the end point mentioned via mps. you can check logs to make sure you have received messages.

NOTE: Make sure to disable your application from connecting directly with kafka.

## For Support

#vajra-onboarding slack channel any assistance.