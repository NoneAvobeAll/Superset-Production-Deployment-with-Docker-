# 1. docker exec -it <superset-container-name> bash
# 2.  superset shell
# 3. paste it and exit. 


from superset import db, security_manager
from flask_appbuilder.security.sqla.models import Role

guest_role = db.session.query(Role).filter_by(name='Guest').first()

if not guest_role:
    print("❌ Guest role not found!")
else:
    print(f"✓ Found Guest role with {len(guest_role.permissions)} current permissions")
    
    # Grant broad permissions
    permissions = [
        ('can_read', 'Chart'),
        ('can_read', 'Dashboard'),
        ('can_explore_json', 'Superset'),
        ('can_explore', 'Superset'),
        ('can_samples', 'Datasource'),
        ('all_datasource_access', 'all_datasource_access'),
        ('all_database_access', 'all_database_access'),
    ]
    
    for perm_name, view_name in permissions:
        pv = security_manager.find_permission_view_menu(perm_name, view_name)
        if pv:
            if pv not in guest_role.permissions:
                guest_role.permissions.append(pv)
                print(f"✓ Added: {perm_name} on {view_name}")
            else:
                print(f"  Already has: {perm_name} on {view_name}")
        else:
            print(f"⚠ Permission not found: {perm_name} on {view_name}")
    
    db.session.commit()
    print(f"\n✅ Done! Guest role now has {len(guest_role.permissions)} permissions")


# 5. restart docker containter 


#6. If needed run the following to ensure critical permissions are present for filters to work
# 6.1. docker exec -it <superset-container-name> bash
# 6.2.  superset shell
# 6.3. paste it and exit.



from superset import db, security_manager
from flask_appbuilder.security.sqla.models import Role

# Get Guest role
guest_role = db.session.query(Role).filter_by(name='Guest').first()

if not guest_role:
    print("ERROR: Guest role not found!")
else:
    print(f"Found Guest role with {len(guest_role.permissions)} permissions")
    
    # Critical permissions for filters to work
    critical_permissions = [
        ('can_write', 'Chart'),  # MUST HAVE for filter interactions
        ('can_write', 'Dashboard'),
        ('can_read', 'Chart'),
        ('can_read', 'Dashboard'),
        ('can_explore_json', 'Superset'),
        ('can_explore', 'Superset'),
        ('can_warm_up_cache', 'Superset'),
        ('can_dashboard_permalink', 'Superset'),
    ]
    
    added_count = 0
    for perm_name, view_name in critical_permissions:
        pv = security_manager.find_permission_view_menu(perm_name, view_name)
        if pv:
            if pv not in guest_role.permissions:
                guest_role.permissions.append(pv)
                print(f"✓ ADDED: {perm_name} on {view_name}")
                added_count += 1
            else:
                print(f"  Has: {perm_name} on {view_name}")
        else:
            # Try to create the permission if it doesn't exist
            try:
                security_manager.add_permission_view_menu(perm_name, view_name)
                pv = security_manager.find_permission_view_menu(perm_name, view_name)
                if pv:
                    guest_role.permissions.append(pv)
                    print(f"✓ CREATED & ADDED: {perm_name} on {view_name}")
                    added_count += 1
            except:
                print(f"⚠ Could not create: {perm_name} on {view_name}")
    
    db.session.commit()
    print(f"\n✅ Added {added_count} new permissions")
    print(f"Guest role now has {len(guest_role.permissions)} total permissions")

exit()
