# DECAMP-2-Project
# DECAMP2 Database Interface

Our goal in this project was to create a user-friendly web interface enabling researchers and students to easily access and analyze the DECAMP2 study data. Our objectives included developing an intuitive interface, setting up a database, and offering data visualization features.

## Project Details

Our main tasks involved:

1. **Database implementation**: Cleaning up the provided data tables and integrating them into a MariaDB database.
2. **User interface development**: Developing a Python Dash-based interface to allow for interactive data visualizations.
3. **Data query functionalities**: Implementing different query methods for the database via the user interface to assist researchers.
4. **Data download feature**: Enabling data to be downloaded to local drives in multiple formats.
5. **External RNA-seq database linkage**: Linking to the external Gene Expression Omnibus RNA-seq database.
6. **Study overview**: Providing a comprehensive overview of the study.
7. **Help pages**: Creating help pages for user support.

These tasks were successfully achieved and implemented in a user-friendly web interface, currently accessible at https://bioed.bu.edu/students_23/Team_G/index.html. 

## Challenges and Solutions

We faced a few challenges during the project:

- We couldn't use the Dash framework due to the limitations of its free version. We instead used Google Charts and Python CGI module to create the web interface.
- We initially planned to restrict access to specific "bu" email addresses. However, we realized that the interface and the database would be uploaded to the lab’s server, and thus, will already be restricted.
- Debugging the Python code was difficult as errors didn't show up on the Bioed error log.

## Team Members and Responsibilities

- Whitney Souery: Database design, query design and implementation
- Irzam Sarfraz: User-interface design, implementation of Google Charts, and database design
- Ojong Tabi: Database design, implementation, table uploads, and query implementation

## Contributors
- Whitney Souery: __________Whitney Souery __________
- Irzam Sarfraz: __________Irzam Sarfraz __________
- Ojong Tabi: __________Ojong Tabi __________

## Acknowledgments
We appreciate the opportunity to contribute to the DECAMP2 study, and hope our interface will facilitate data access and research.
