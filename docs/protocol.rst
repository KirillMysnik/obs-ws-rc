Protocol Reference
==================

Types
-----

bool
++++



- **Style:** This type is native to Python


float
+++++



- **Style:** This type is native to Python


int
+++



- **Style:** This type is native to Python


str
+++



- **Style:** This type is native to Python


Font
++++



- **Style:** This type contains statically typed fields




- **Fields:**




  - FACE




    - **type:** `str`_
    - **pythonic name:** ``face``
    - **internal name:** *face*
    - **is optional?** Yes




  - FLAGS




    - **type:** `int`_
    - **pythonic name:** ``flags``
    - **internal name:** *flags*
    - **is optional?** Yes




  - SIZE




    - **type:** `int`_
    - **pythonic name:** ``size``
    - **internal name:** *size*
    - **is optional?** Yes




  - STYLE




    - **type:** `str`_
    - **pythonic name:** ``style``
    - **internal name:** *style*
    - **is optional?** Yes


Profile
+++++++



- **Style:** This type contains statically typed fields




- **Fields:**




  - PROFILE NAME




    - **type:** `str`_
    - **pythonic name:** ``profile_name``
    - **internal name:** *profile-name*
    - **is optional?** No


profile_list
++++++++++++



- **Style:** This type represents a list of objects of other type




- **Item type:** `Profile`_


scene_collection_list
+++++++++++++++++++++



- **Style:** This type represents a list of objects of other type




- **Item type:** `SceneCollection`_


scene_list
++++++++++



- **Style:** This type represents a list of objects of other type




- **Item type:** `source_list`_


SceneCollection
+++++++++++++++



- **Style:** This type contains statically typed fields




- **Fields:**




  - SC NAME




    - **type:** `str`_
    - **pythonic name:** ``sc_name``
    - **internal name:** *sc-name*
    - **is optional?** No


SceneSource
+++++++++++



- **Style:** This type contains statically typed fields




- **Fields:**




  - NAME




    - **type:** `str`_
    - **pythonic name:** ``name``
    - **internal name:** *name*
    - **is optional?** No




  - TYPE




    - **type:** `str`_
    - **pythonic name:** ``type``
    - **internal name:** *type*
    - **is optional?** No




  - VOLUME




    - **type:** `float`_
    - **pythonic name:** ``volume``
    - **internal name:** *volume*
    - **is optional?** No




  - X




    - **type:** `float`_
    - **pythonic name:** ``x``
    - **internal name:** *x*
    - **is optional?** No




  - Y




    - **type:** `float`_
    - **pythonic name:** ``y``
    - **internal name:** *y*
    - **is optional?** No




  - SOURCE CX




    - **type:** `int`_
    - **pythonic name:** ``source_cx``
    - **internal name:** *source_cx*
    - **is optional?** No




  - SOURCE CY




    - **type:** `int`_
    - **pythonic name:** ``source_cy``
    - **internal name:** *source_cy*
    - **is optional?** No




  - CX




    - **type:** `float`_
    - **pythonic name:** ``cx``
    - **internal name:** *cx*
    - **is optional?** No




  - CY




    - **type:** `float`_
    - **pythonic name:** ``cy``
    - **internal name:** *cy*
    - **is optional?** No




  - RENDER




    - **type:** `bool`_
    - **pythonic name:** ``render``
    - **internal name:** *render*
    - **is optional?** No


source_list
+++++++++++



- **Style:** This type represents a list of objects of other type




- **Item type:** `SceneSource`_


Stream
++++++



- **Style:** This type contains statically typed fields




- **Fields:**




  - SETTINGS




    - **type:** `StreamSettings`_
    - **pythonic name:** ``settings``
    - **internal name:** *settings*
    - **is optional?** Yes




  - TYPE




    - **type:** `str`_
    - **pythonic name:** ``type``
    - **internal name:** *type*
    - **is optional?** Yes




  - METADATA




    - **type:** `StreamMetadata`_
    - **pythonic name:** ``metadata``
    - **internal name:** *metadata*
    - **is optional?** Yes


StreamMetadata
++++++++++++++



- **Style:** The number and types of the fields can vary




- **Allowed types:** `str`_ `float`_ `int`_ `bool`_


StreamSettings
++++++++++++++



- **Style:** This type contains statically typed fields




- **Fields:**




  - SERVER




    - **type:** `str`_
    - **pythonic name:** ``server``
    - **internal name:** *server*
    - **is optional?** Yes




  - KEY




    - **type:** `str`_
    - **pythonic name:** ``key``
    - **internal name:** *key*
    - **is optional?** Yes




  - USE AUTH




    - **type:** `bool`_
    - **pythonic name:** ``use_auth``
    - **internal name:** *use-auth*
    - **is optional?** Yes




  - USERNAME




    - **type:** `str`_
    - **pythonic name:** ``username``
    - **internal name:** *username*
    - **is optional?** Yes




  - PASSWORD




    - **type:** `str`_
    - **pythonic name:** ``password``
    - **internal name:** *password*
    - **is optional?** Yes


Transition
++++++++++



- **Style:** This type contains statically typed fields




- **Fields:**




  - NAME




    - **type:** `str`_
    - **pythonic name:** ``name``
    - **internal name:** *name*
    - **is optional?** Yes




  - DURATION




    - **type:** `int`_
    - **pythonic name:** ``duration``
    - **internal name:** *duration*
    - **is optional?** Yes


transition_name_list
++++++++++++++++++++



- **Style:** This type represents a list of objects of other type




- **Item type:** `TransitionName`_


TransitionName
++++++++++++++



- **Style:** This type contains statically typed fields




- **Fields:**




  - NAME




    - **type:** `str`_
    - **pythonic name:** ``name``
    - **internal name:** *name*
    - **is optional?** No


Requests
--------

Authenticate
++++++++++++



- **Description:** `view PROTOCOL.md entry on 'Authenticate' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#authenticate>`_




- **Request Fields:**




  - AUTH




    - **type:** `str`_
    - **pythonic name:** ``auth``
    - **internal name:** *auth*
    - **is optional?** No




- **Response Fields:**


DisableStudioMode
+++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'DisableStudioMode' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#disablestudiomode>`_




- **Request Fields:**




- **Response Fields:**


EnableStudioMode
++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'EnableStudioMode' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#enablestudiomode>`_




- **Request Fields:**




- **Response Fields:**


GetAuthRequired
+++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'GetAuthRequired' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#getauthrequired>`_




- **Request Fields:**




- **Response Fields:**




  - AUTH REQUIRED




    - **type:** `bool`_
    - **pythonic name:** ``auth_required``
    - **internal name:** *authRequired*
    - **is optional?** No




  - CHALLENGE




    - **type:** `str`_
    - **pythonic name:** ``challenge``
    - **internal name:** *challenge*
    - **is optional?** Yes




  - SALT




    - **type:** `str`_
    - **pythonic name:** ``salt``
    - **internal name:** *salt*
    - **is optional?** Yes


GetCurrentProfile
+++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'GetCurrentProfile' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#getcurrentprofile>`_




- **Request Fields:**




- **Response Fields:**




  - PROFILE NAME




    - **type:** `str`_
    - **pythonic name:** ``profile_name``
    - **internal name:** *profile-name*
    - **is optional?** No


GetCurrentScene
+++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'GetCurrentScene' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#getcurrentscene>`_




- **Request Fields:**




- **Response Fields:**




  - NAME




    - **type:** `str`_
    - **pythonic name:** ``name``
    - **internal name:** *name*
    - **is optional?** No




  - SOURCES




    - **type:** `source_list`_
    - **pythonic name:** ``sources``
    - **internal name:** *sources*
    - **is optional?** No


GetCurrentSceneCollection
+++++++++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'GetCurrentSceneCollection' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#getcurrentscenecollection>`_




- **Request Fields:**




- **Response Fields:**




  - SC NAME




    - **type:** `str`_
    - **pythonic name:** ``sc_name``
    - **internal name:** *sc-name*
    - **is optional?** No


GetCurrentTransition
++++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'GetCurrentTransition' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#getcurrenttransition>`_




- **Request Fields:**




- **Response Fields:**




  - NAME




    - **type:** `str`_
    - **pythonic name:** ``name``
    - **internal name:** *name*
    - **is optional?** No




  - DURATION




    - **type:** `int`_
    - **pythonic name:** ``duration``
    - **internal name:** *duration*
    - **is optional?** Yes


GetMute
+++++++



- **Description:** `view PROTOCOL.md entry on 'GetMute' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#getmute>`_




- **Request Fields:**




  - SOURCE




    - **type:** `str`_
    - **pythonic name:** ``source``
    - **internal name:** *source*
    - **is optional?** No




- **Response Fields:**




  - NAME




    - **type:** `str`_
    - **pythonic name:** ``name``
    - **internal name:** *name*
    - **is optional?** No




  - MUTED




    - **type:** `bool`_
    - **pythonic name:** ``muted``
    - **internal name:** *muted*
    - **is optional?** No


GetPreviewScene
+++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'GetPreviewScene' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#getpreviewscene>`_




- **Request Fields:**




- **Response Fields:**




  - NAME




    - **type:** `str`_
    - **pythonic name:** ``name``
    - **internal name:** *name*
    - **is optional?** No




  - SOURCES




    - **type:** `source_list`_
    - **pythonic name:** ``sources``
    - **internal name:** *sources*
    - **is optional?** No


GetRecordingFolder
++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'GetRecordingFolder' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#getrecordingfolder>`_




- **Request Fields:**




- **Response Fields:**




  - REC FOLDER




    - **type:** `str`_
    - **pythonic name:** ``rec_folder``
    - **internal name:** *rec-folder*
    - **is optional?** No


GetSceneList
++++++++++++



- **Description:** `view PROTOCOL.md entry on 'GetSceneList' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#getscenelist>`_




- **Request Fields:**




- **Response Fields:**




  - CURRENT SCENE




    - **type:** `str`_
    - **pythonic name:** ``current_scene``
    - **internal name:** *current-scene*
    - **is optional?** No




  - SCENES




    - **type:** `scene_list`_
    - **pythonic name:** ``scenes``
    - **internal name:** *scenes*
    - **is optional?** No


GetSpecialSources
+++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'GetSpecialSources' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#getspecialsources>`_




- **Request Fields:**




- **Response Fields:**




  - DESKTOP1




    - **type:** `str`_
    - **pythonic name:** ``desktop1``
    - **internal name:** *desktop-1*
    - **is optional?** Yes




  - DESKTOP2




    - **type:** `str`_
    - **pythonic name:** ``desktop2``
    - **internal name:** *desktop-2*
    - **is optional?** Yes




  - MIC1




    - **type:** `str`_
    - **pythonic name:** ``mic1``
    - **internal name:** *mic-1*
    - **is optional?** Yes




  - MIC2




    - **type:** `str`_
    - **pythonic name:** ``mic2``
    - **internal name:** *mic-2*
    - **is optional?** Yes




  - MIC3




    - **type:** `str`_
    - **pythonic name:** ``mic3``
    - **internal name:** *mic-3*
    - **is optional?** Yes


GetStreamingStatus
++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'GetStreamingStatus' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#getstreamingstatus>`_




- **Request Fields:**




- **Response Fields:**




  - STREAMING




    - **type:** `bool`_
    - **pythonic name:** ``streaming``
    - **internal name:** *streaming*
    - **is optional?** No




  - RECORDING




    - **type:** `bool`_
    - **pythonic name:** ``recording``
    - **internal name:** *recording*
    - **is optional?** No




  - STREAM TIMECODE




    - **type:** `str`_
    - **pythonic name:** ``stream_timecode``
    - **internal name:** *stream-timecode*
    - **is optional?** Yes




  - REC TIMECODE




    - **type:** `str`_
    - **pythonic name:** ``rec_timecode``
    - **internal name:** *rec-timecode*
    - **is optional?** Yes




  - PREVIEW ONLY




    - **type:** `bool`_
    - **pythonic name:** ``preview_only``
    - **internal name:** *preview-only*
    - **is optional?** No


GetStreamSettings
+++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'GetStreamSettings' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#getstreamsettings>`_




- **Request Fields:**




- **Response Fields:**




  - TYPE




    - **type:** `str`_
    - **pythonic name:** ``type``
    - **internal name:** *type*
    - **is optional?** No




  - SETTINGS




    - **type:** `StreamSettings`_
    - **pythonic name:** ``settings``
    - **internal name:** *settings*
    - **is optional?** No


GetStudioModeStatus
+++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'GetStudioModeStatus' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#getstudiomodestatus>`_




- **Request Fields:**




- **Response Fields:**




  - STUDIO MODE




    - **type:** `bool`_
    - **pythonic name:** ``studio_mode``
    - **internal name:** *studio-mode*
    - **is optional?** No


GetTextGDIPlusProperties
++++++++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'GetTextGDIPlusProperties' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#gettextgdiplusproperties>`_




- **Request Fields:**




  - SOURCE




    - **type:** `str`_
    - **pythonic name:** ``source``
    - **internal name:** *source*
    - **is optional?** No




  - SCENE NAME




    - **type:** `str`_
    - **pythonic name:** ``scene_name``
    - **internal name:** *scene-name*
    - **is optional?** Yes




- **Response Fields:**




  - ALIGN




    - **type:** `str`_
    - **pythonic name:** ``align``
    - **internal name:** *align*
    - **is optional?** No




  - BK COLOR




    - **type:** `int`_
    - **pythonic name:** ``bk_color``
    - **internal name:** *bk_color*
    - **is optional?** No




  - BK OPACITY




    - **type:** `int`_
    - **pythonic name:** ``bk_opacity``
    - **internal name:** *bk_opacity*
    - **is optional?** No




  - CHATLOG




    - **type:** `bool`_
    - **pythonic name:** ``chatlog``
    - **internal name:** *chatlog*
    - **is optional?** No




  - CHATLOG LINES




    - **type:** `int`_
    - **pythonic name:** ``chatlog_lines``
    - **internal name:** *chatlog_lines*
    - **is optional?** No




  - COLOR




    - **type:** `int`_
    - **pythonic name:** ``color``
    - **internal name:** *color*
    - **is optional?** No




  - EXTENTS




    - **type:** `bool`_
    - **pythonic name:** ``extents``
    - **internal name:** *extents*
    - **is optional?** No




  - EXTENTS WRAP




    - **type:** `bool`_
    - **pythonic name:** ``extents_wrap``
    - **internal name:** *extents_wrap*
    - **is optional?** No




  - EXTENTS CX




    - **type:** `int`_
    - **pythonic name:** ``extents_cx``
    - **internal name:** *extents_cx*
    - **is optional?** No




  - EXTENTS CY




    - **type:** `int`_
    - **pythonic name:** ``extents_cy``
    - **internal name:** *extents_cy*
    - **is optional?** No




  - FILE




    - **type:** `str`_
    - **pythonic name:** ``file``
    - **internal name:** *file*
    - **is optional?** No




  - READ FROM FILE




    - **type:** `bool`_
    - **pythonic name:** ``read_from_file``
    - **internal name:** *read_from_file*
    - **is optional?** No




  - FONT




    - **type:** `Font`_
    - **pythonic name:** ``font``
    - **internal name:** *font*
    - **is optional?** No




  - GRADIENT




    - **type:** `bool`_
    - **pythonic name:** ``gradient``
    - **internal name:** *gradient*
    - **is optional?** No




  - GRADIENT COLOR




    - **type:** `int`_
    - **pythonic name:** ``gradient_color``
    - **internal name:** *gradient_color*
    - **is optional?** No




  - GRADIENT DIR




    - **type:** `float`_
    - **pythonic name:** ``gradient_dir``
    - **internal name:** *gradient_dir*
    - **is optional?** No




  - GRADIENT OPACITY




    - **type:** `int`_
    - **pythonic name:** ``gradient_opacity``
    - **internal name:** *gradient_opacity*
    - **is optional?** No




  - OUTLINE




    - **type:** `bool`_
    - **pythonic name:** ``outline``
    - **internal name:** *outline*
    - **is optional?** No




  - OUTLINE COLOR




    - **type:** `int`_
    - **pythonic name:** ``outline_color``
    - **internal name:** *outline_color*
    - **is optional?** No




  - OUTLINE SIZE




    - **type:** `int`_
    - **pythonic name:** ``outline_size``
    - **internal name:** *outline_size*
    - **is optional?** No




  - OUTLINE OPACITY




    - **type:** `int`_
    - **pythonic name:** ``outline_opacity``
    - **internal name:** *outline_opacity*
    - **is optional?** No




  - TEXT




    - **type:** `str`_
    - **pythonic name:** ``text``
    - **internal name:** *text*
    - **is optional?** No




  - VALIGN




    - **type:** `bool`_
    - **pythonic name:** ``valign``
    - **internal name:** *valign*
    - **is optional?** No




  - VERTICAL




    - **type:** `bool`_
    - **pythonic name:** ``vertical``
    - **internal name:** *vertical*
    - **is optional?** No




  - RENDER




    - **type:** `bool`_
    - **pythonic name:** ``render``
    - **internal name:** *render*
    - **is optional?** No


GetTransitionDuration
+++++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'GetTransitionDuration' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#gettransitionduration>`_




- **Request Fields:**




- **Response Fields:**




  - TRANSITION DURATION




    - **type:** `int`_
    - **pythonic name:** ``transition_duration``
    - **internal name:** *transition-duration*
    - **is optional?** No


GetTransitionList
+++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'GetTransitionList' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#gettransitionlist>`_




- **Request Fields:**




- **Response Fields:**




  - CURRENT TRANSITION




    - **type:** `str`_
    - **pythonic name:** ``current_transition``
    - **internal name:** *current-transition*
    - **is optional?** No




  - TRANSITIONS




    - **type:** `transition_name_list`_
    - **pythonic name:** ``transitions``
    - **internal name:** *transitions*
    - **is optional?** No


GetVersion
++++++++++



- **Description:** `view PROTOCOL.md entry on 'GetVersion' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#getversion>`_




- **Request Fields:**




- **Response Fields:**




  - VERSION




    - **type:** `float`_
    - **pythonic name:** ``version``
    - **internal name:** *version*
    - **is optional?** No




  - OBS WEBSOCKET VERSION




    - **type:** `str`_
    - **pythonic name:** ``obs_websocket_version``
    - **internal name:** *obs-websocket-version*
    - **is optional?** No




  - OBS STUDIO VERSION




    - **type:** `str`_
    - **pythonic name:** ``obs_studio_version``
    - **internal name:** *obs-studio-version*
    - **is optional?** No


GetVolume
+++++++++



- **Description:** `view PROTOCOL.md entry on 'GetVolume' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#getvolume>`_




- **Request Fields:**




  - SOURCE




    - **type:** `str`_
    - **pythonic name:** ``source``
    - **internal name:** *source*
    - **is optional?** No




- **Response Fields:**




  - NAME




    - **type:** `str`_
    - **pythonic name:** ``name``
    - **internal name:** *name*
    - **is optional?** No




  - VOLUME




    - **type:** `float`_
    - **pythonic name:** ``volume``
    - **internal name:** *volume*
    - **is optional?** No




  - MUTED




    - **type:** `bool`_
    - **pythonic name:** ``muted``
    - **internal name:** *muted*
    - **is optional?** No


ListProfiles
++++++++++++



- **Description:** `view PROTOCOL.md entry on 'ListProfiles' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#listprofiles>`_




- **Request Fields:**




- **Response Fields:**




  - PROFILES




    - **type:** `profile_list`_
    - **pythonic name:** ``profiles``
    - **internal name:** *profiles*
    - **is optional?** No


ListSceneCollections
++++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'ListSceneCollections' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#listscenecollections>`_




- **Request Fields:**




- **Response Fields:**




  - SCENE COLLECTIONS




    - **type:** `scene_collection_list`_
    - **pythonic name:** ``scene_collections``
    - **internal name:** *scene-collections*
    - **is optional?** No


SaveStreamSettings
++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SaveStreamSettings' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#savestreamsettings>`_




- **Request Fields:**




- **Response Fields:**


SetCurrentProfile
+++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SetCurrentProfile' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#setcurrentprofile>`_




- **Request Fields:**




  - PROFILE NAME




    - **type:** `str`_
    - **pythonic name:** ``profile_name``
    - **internal name:** *profile-name*
    - **is optional?** No




- **Response Fields:**


SetCurrentScene
+++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SetCurrentScene' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#setcurrentscene>`_




- **Request Fields:**




  - SCENE NAME




    - **type:** `str`_
    - **pythonic name:** ``scene_name``
    - **internal name:** *scene-name*
    - **is optional?** No




- **Response Fields:**


SetCurrentSceneCollection
+++++++++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SetCurrentSceneCollection' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#setcurrentscenecollection>`_




- **Request Fields:**




  - SC NAME




    - **type:** `str`_
    - **pythonic name:** ``sc_name``
    - **internal name:** *sc-name*
    - **is optional?** No




- **Response Fields:**


SetCurrentTransition
++++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SetCurrentTransition' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#setcurrenttransition>`_




- **Request Fields:**




  - TRANSITION NAME




    - **type:** `str`_
    - **pythonic name:** ``transition_name``
    - **internal name:** *transition-name*
    - **is optional?** No




- **Response Fields:**


SetMute
+++++++



- **Description:** `view PROTOCOL.md entry on 'SetMute' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#setmute>`_




- **Request Fields:**




  - SOURCE




    - **type:** `str`_
    - **pythonic name:** ``source``
    - **internal name:** *source*
    - **is optional?** No




  - MUTE




    - **type:** `bool`_
    - **pythonic name:** ``mute``
    - **internal name:** *mute*
    - **is optional?** No




- **Response Fields:**


SetPreviewScene
+++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SetPreviewScene' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#setpreviewscene>`_




- **Request Fields:**




  - SCENE NAME




    - **type:** `str`_
    - **pythonic name:** ``scene_name``
    - **internal name:** *scene-name*
    - **is optional?** No




- **Response Fields:**


SetRecordingFolder
++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SetRecordingFolder' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#setrecordingfolder>`_




- **Request Fields:**




  - REC FOLDER




    - **type:** `str`_
    - **pythonic name:** ``rec_folder``
    - **internal name:** *rec-folder*
    - **is optional?** No




- **Response Fields:**


SetSceneItemCrop
++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SetSceneItemCrop' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#setsceneitemcrop>`_




- **Request Fields:**




  - ITEM




    - **type:** `str`_
    - **pythonic name:** ``item``
    - **internal name:** *item*
    - **is optional?** No




  - SCENE NAME




    - **type:** `str`_
    - **pythonic name:** ``scene_name``
    - **internal name:** *scene-name*
    - **is optional?** No




  - TOP




    - **type:** `int`_
    - **pythonic name:** ``top``
    - **internal name:** *top*
    - **is optional?** No




  - BOTTOM




    - **type:** `int`_
    - **pythonic name:** ``bottom``
    - **internal name:** *bottom*
    - **is optional?** No




  - LEFT




    - **type:** `int`_
    - **pythonic name:** ``left``
    - **internal name:** *left*
    - **is optional?** No




  - RIGHT




    - **type:** `int`_
    - **pythonic name:** ``right``
    - **internal name:** *right*
    - **is optional?** No




- **Response Fields:**


SetSceneItemPosition
++++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SetSceneItemPosition' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#setsceneitemposition>`_




- **Request Fields:**




  - ITEM




    - **type:** `str`_
    - **pythonic name:** ``item``
    - **internal name:** *item*
    - **is optional?** No




  - X




    - **type:** `float`_
    - **pythonic name:** ``x``
    - **internal name:** *x*
    - **is optional?** No




  - Y




    - **type:** `float`_
    - **pythonic name:** ``y``
    - **internal name:** *y*
    - **is optional?** No




  - SCENE NAME




    - **type:** `str`_
    - **pythonic name:** ``scene_name``
    - **internal name:** *scene-name*
    - **is optional?** No




- **Response Fields:**


SetSceneItemTransform
+++++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SetSceneItemTransform' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#setsceneitemtransform>`_




- **Request Fields:**




  - ITEM




    - **type:** `str`_
    - **pythonic name:** ``item``
    - **internal name:** *item*
    - **is optional?** No




  - X SCALE




    - **type:** `float`_
    - **pythonic name:** ``x_scale``
    - **internal name:** *x-scale*
    - **is optional?** No




  - Y SCALE




    - **type:** `float`_
    - **pythonic name:** ``y_scale``
    - **internal name:** *y-scale*
    - **is optional?** No




  - ROTATION




    - **type:** `float`_
    - **pythonic name:** ``rotation``
    - **internal name:** *rotation*
    - **is optional?** No




  - SCENE NAME




    - **type:** `str`_
    - **pythonic name:** ``scene_name``
    - **internal name:** *scene-name*
    - **is optional?** No




- **Response Fields:**


SetSourceRender
+++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SetSourceRender' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#setsourcerender>`_




- **Request Fields:**




  - SOURCE




    - **type:** `str`_
    - **pythonic name:** ``source``
    - **internal name:** *source*
    - **is optional?** No




  - RENDER




    - **type:** `bool`_
    - **pythonic name:** ``render``
    - **internal name:** *render*
    - **is optional?** No




  - SCENE NAME




    - **type:** `str`_
    - **pythonic name:** ``scene_name``
    - **internal name:** *scene-name*
    - **is optional?** Yes




- **Response Fields:**


SetStreamSettings
+++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SetStreamSettings' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#setstreamsettings>`_




- **Request Fields:**




  - TYPE




    - **type:** `str`_
    - **pythonic name:** ``type``
    - **internal name:** *type*
    - **is optional?** No




  - SETTINGS




    - **type:** `StreamSettings`_
    - **pythonic name:** ``settings``
    - **internal name:** *settings*
    - **is optional?** No




  - SAVE




    - **type:** `bool`_
    - **pythonic name:** ``save``
    - **internal name:** *save*
    - **is optional?** No




- **Response Fields:**




  - TYPE




    - **type:** `str`_
    - **pythonic name:** ``type``
    - **internal name:** *type*
    - **is optional?** No




  - SETTINGS




    - **type:** `StreamSettings`_
    - **pythonic name:** ``settings``
    - **internal name:** *settings*
    - **is optional?** No


SetTransitionDuration
+++++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SetTransitionDuration' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#settransitionduration>`_




- **Request Fields:**




  - DURATION




    - **type:** `int`_
    - **pythonic name:** ``duration``
    - **internal name:** *duration*
    - **is optional?** No




- **Response Fields:**


SetVolume
+++++++++



- **Description:** `view PROTOCOL.md entry on 'SetVolume' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#setvolume>`_




- **Request Fields:**




  - SOURCE




    - **type:** `str`_
    - **pythonic name:** ``source``
    - **internal name:** *source*
    - **is optional?** No




  - VOLUME




    - **type:** `float`_
    - **pythonic name:** ``volume``
    - **internal name:** *volume*
    - **is optional?** No




- **Response Fields:**


StartRecording
++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'StartRecording' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#startrecording>`_




- **Request Fields:**




- **Response Fields:**


StartStopRecording
++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'StartStopRecording' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#startstoprecording>`_




- **Request Fields:**




  - STREAM




    - **type:** `Stream`_
    - **pythonic name:** ``stream``
    - **internal name:** *stream*
    - **is optional?** Yes




- **Response Fields:**


StartStopStreaming
++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'StartStopStreaming' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#startstopstreaming>`_




- **Request Fields:**




- **Response Fields:**


StartStreaming
++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'StartStreaming' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#startstreaming>`_




- **Request Fields:**




  - STREAM




    - **type:** `Stream`_
    - **pythonic name:** ``stream``
    - **internal name:** *stream*
    - **is optional?** Yes




- **Response Fields:**


StopRecording
+++++++++++++



- **Description:** `view PROTOCOL.md entry on 'StopRecording' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#stoprecording>`_




- **Request Fields:**




- **Response Fields:**


StopStreaming
+++++++++++++



- **Description:** `view PROTOCOL.md entry on 'StopStreaming' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#stopstreaming>`_




- **Request Fields:**




- **Response Fields:**


ToggleMute
++++++++++



- **Description:** `view PROTOCOL.md entry on 'ToggleMute' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#togglemute>`_




- **Request Fields:**




  - SOURCE




    - **type:** `str`_
    - **pythonic name:** ``source``
    - **internal name:** *source*
    - **is optional?** No




- **Response Fields:**


ToggleStudioMode
++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'ToggleStudioMode' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#togglestudiomode>`_




- **Request Fields:**




- **Response Fields:**


TransitionToProgram
+++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'TransitionToProgram' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#transitiontoprogram>`_




- **Request Fields:**




  - WITH TRANSITION




    - **type:** `Transition`_
    - **pythonic name:** ``with_transition``
    - **internal name:** *with-transition*
    - **is optional?** No




- **Response Fields:**


Events
------

Exiting
+++++++



- **Description:** `view PROTOCOL.md entry on 'Exiting' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#exiting>`_




- **Request Fields:**




- **Response Fields:**


PreviewSceneChanged
+++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'PreviewSceneChanged' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#previewscenechanged>`_




- **Request Fields:**




  - SCENE NAME




    - **type:** `str`_
    - **pythonic name:** ``scene_name``
    - **internal name:** *scene-name*
    - **is optional?** No




  - SOURCES




    - **type:** `source_list`_
    - **pythonic name:** ``sources``
    - **internal name:** *sources*
    - **is optional?** No




- **Response Fields:**


ProfileChanged
++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'ProfileChanged' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#profilechanged>`_




- **Request Fields:**




- **Response Fields:**


ProfileListChanged
++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'ProfileListChanged' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#profilelistchanged>`_




- **Request Fields:**




- **Response Fields:**


RecordingStarted
++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'RecordingStarted' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#recordingstarted>`_




- **Request Fields:**




- **Response Fields:**


RecordingStarting
+++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'RecordingStarting' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#recordingstarting>`_




- **Request Fields:**




- **Response Fields:**


RecordingStopped
++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'RecordingStopped' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#recordingstopped>`_




- **Request Fields:**




- **Response Fields:**


RecordingStopping
+++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'RecordingStopping' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#recordingstopping>`_




- **Request Fields:**




- **Response Fields:**


SceneCollectionChanged
++++++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SceneCollectionChanged' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#scenecollectionchanged>`_




- **Request Fields:**




- **Response Fields:**


SceneCollectionListChanged
++++++++++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SceneCollectionListChanged' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#scenecollectionlistchanged>`_




- **Request Fields:**




- **Response Fields:**


SceneItemAdded
++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SceneItemAdded' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#sceneitemadded>`_




- **Request Fields:**




  - SCENE NAME




    - **type:** `str`_
    - **pythonic name:** ``scene_name``
    - **internal name:** *scene-name*
    - **is optional?** No




  - ITEM NAME




    - **type:** `str`_
    - **pythonic name:** ``item_name``
    - **internal name:** *item-name*
    - **is optional?** No




- **Response Fields:**


SceneItemRemoved
++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SceneItemRemoved' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#sceneitemremoved>`_




- **Request Fields:**




  - SCENE NAME




    - **type:** `str`_
    - **pythonic name:** ``scene_name``
    - **internal name:** *scene-name*
    - **is optional?** No




  - ITEM NAME




    - **type:** `str`_
    - **pythonic name:** ``item_name``
    - **internal name:** *item-name*
    - **is optional?** No




- **Response Fields:**


SceneItemVisibilityChanged
++++++++++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SceneItemVisibilityChanged' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#sceneitemvisibilitychanged>`_




- **Request Fields:**




  - SCENE NAME




    - **type:** `str`_
    - **pythonic name:** ``scene_name``
    - **internal name:** *scene-name*
    - **is optional?** No




  - ITEM NAME




    - **type:** `str`_
    - **pythonic name:** ``item_name``
    - **internal name:** *item-name*
    - **is optional?** No




  - ITEM VISIBLE




    - **type:** `bool`_
    - **pythonic name:** ``item_visible``
    - **internal name:** *item-visible*
    - **is optional?** No




- **Response Fields:**


ScenesChanged
+++++++++++++



- **Description:** `view PROTOCOL.md entry on 'ScenesChanged' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#sceneschanged>`_




- **Request Fields:**




- **Response Fields:**


SourceOrderChanged
++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SourceOrderChanged' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#sourceorderchanged>`_




- **Request Fields:**




  - SCENE NAME




    - **type:** `str`_
    - **pythonic name:** ``scene_name``
    - **internal name:** *scene-name*
    - **is optional?** No




- **Response Fields:**


StreamStarted
+++++++++++++



- **Description:** `view PROTOCOL.md entry on 'StreamStarted' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#streamstarted>`_




- **Request Fields:**




- **Response Fields:**


StreamStarting
++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'StreamStarting' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#streamstarting>`_




- **Request Fields:**




  - PREVIEW ONLY




    - **type:** `bool`_
    - **pythonic name:** ``preview_only``
    - **internal name:** *preview-only*
    - **is optional?** No




- **Response Fields:**


StreamStatus
++++++++++++



- **Description:** `view PROTOCOL.md entry on 'StreamStatus' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#streamstatus>`_




- **Request Fields:**




  - STREAMING




    - **type:** `bool`_
    - **pythonic name:** ``streaming``
    - **internal name:** *streaming*
    - **is optional?** No




  - RECORDING




    - **type:** `bool`_
    - **pythonic name:** ``recording``
    - **internal name:** *recording*
    - **is optional?** No




  - PREVIEW ONLY




    - **type:** `bool`_
    - **pythonic name:** ``preview_only``
    - **internal name:** *preview-only*
    - **is optional?** No




  - BYTES PER SEC




    - **type:** `int`_
    - **pythonic name:** ``bytes_per_sec``
    - **internal name:** *bytes-per-sec*
    - **is optional?** No




  - KBITS PER SEC




    - **type:** `int`_
    - **pythonic name:** ``kbits_per_sec``
    - **internal name:** *kbits-per-sec*
    - **is optional?** No




  - STRAIN




    - **type:** `float`_
    - **pythonic name:** ``strain``
    - **internal name:** *strain*
    - **is optional?** No




  - TOTAL STREAM TIME




    - **type:** `int`_
    - **pythonic name:** ``total_stream_time``
    - **internal name:** *total-stream-time*
    - **is optional?** No




  - NUM TOTAL FRAMES




    - **type:** `int`_
    - **pythonic name:** ``num_total_frames``
    - **internal name:** *num-total-frames*
    - **is optional?** No




  - NUM DROPPED FRAMES




    - **type:** `int`_
    - **pythonic name:** ``num_dropped_frames``
    - **internal name:** *num-dropped-frames*
    - **is optional?** No




  - FPS




    - **type:** `float`_
    - **pythonic name:** ``fps``
    - **internal name:** *fps*
    - **is optional?** No




- **Response Fields:**


StreamStopped
+++++++++++++



- **Description:** `view PROTOCOL.md entry on 'StreamStopped' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#streamstopped>`_




- **Request Fields:**




- **Response Fields:**


StreamStopping
++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'StreamStopping' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#streamstopping>`_




- **Request Fields:**




  - PREVIEW ONLY




    - **type:** `bool`_
    - **pythonic name:** ``preview_only``
    - **internal name:** *preview-only*
    - **is optional?** No




- **Response Fields:**


StudioModeSwitched
++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'StudioModeSwitched' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#studiomodeswitched>`_




- **Request Fields:**




  - NEW STATE




    - **type:** `bool`_
    - **pythonic name:** ``new_state``
    - **internal name:** *new-state*
    - **is optional?** No




- **Response Fields:**


SwitchScenes
++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SwitchScenes' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#switchscenes>`_




- **Request Fields:**




  - SCENE NAME




    - **type:** `str`_
    - **pythonic name:** ``scene_name``
    - **internal name:** *scene-name*
    - **is optional?** No




  - SOURCES




    - **type:** `source_list`_
    - **pythonic name:** ``sources``
    - **internal name:** *sources*
    - **is optional?** No




- **Response Fields:**


SwitchTransition
++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'SwitchTransition' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#switchtransition>`_




- **Request Fields:**




  - TRANSITION NAME




    - **type:** `str`_
    - **pythonic name:** ``transition_name``
    - **internal name:** *transition-name*
    - **is optional?** No




- **Response Fields:**


TransitionBegin
+++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'TransitionBegin' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#transitionbegin>`_




- **Request Fields:**




  - NAME




    - **type:** `str`_
    - **pythonic name:** ``name``
    - **internal name:** *name*
    - **is optional?** No




  - DURATION




    - **type:** `int`_
    - **pythonic name:** ``duration``
    - **internal name:** *duration*
    - **is optional?** No




- **Response Fields:**


TransitionDurationChanged
+++++++++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'TransitionDurationChanged' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#transitiondurationchanged>`_




- **Request Fields:**




  - NEW DURATION




    - **type:** `int`_
    - **pythonic name:** ``new_duration``
    - **internal name:** *new-duration*
    - **is optional?** No




- **Response Fields:**


TransitionListChanged
+++++++++++++++++++++



- **Description:** `view PROTOCOL.md entry on 'TransitionListChanged' <https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md#transitionlistchanged>`_




- **Request Fields:**




- **Response Fields:**


