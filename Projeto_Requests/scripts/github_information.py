from data_pipeline import Repository_Data

create_object = Repository_Data('google')
information = create_object.get_repo_data('language')
print(information)
