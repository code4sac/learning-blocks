# Canvas LMS API

**API Base URL**: `url = "https://canvas.example.com/api/v1/"`

This is where the specific endpoints must be concatenated at.

## Authentication

Ensure that an API Token has been obtained before sending requests, and define them as such: `headers = {'Authorization': 'Bearer [api_token_here]'}`

## Sending Requests

Using the Requests dependency to fetch data as a JSON object: `requests.get(url, headers=headers)`

# Assignments
An assignment object looks like this:
```js
{
  "id": 4,
  "name": "some assignment",
  "description": "<p>Do the following:</p>...",
  "created_at": "2012-07-01T23:59:00-06:00",
  "updated_at": "2012-07-01T23:59:00-06:00",
  "due_at": "2012-07-01T23:59:00-06:00",
  // Other properties
}
```

## GET

**List all assignments** 
`/courses/:course_id/assignments`

**Get a single assignment** 
`/courses/:course_id/assignments/:id`

**List assignments per user** 
`users/:user_id/courses/:course_id/assignments`

## POST

>One of student_ids, group_id, or course_section_id must be present. At most one should be present; if multiple are present only the most specific (student_ids first, then group_id, then course_section_id) is used and any others are ignored.

**Create an assignment** 
`/courses/:course_id/assignments`

**Duplicate assignment** `/courses/:course_id/assignments/:assignment_id/duplicate`

**Create an assignment override** 
`courses/:course_id/assignments/:assignment_id/overrides`

**Batch create overrides in a course** 
`courses/:course_id/assignments/overrides`

Creates the specified overrides for each assignment. Handles creation in a transaction, so all records are created or none are.

# Discussion
A discussion object looks like this:
```js
{
  "id": 1,
  "title": "Topic 1",
  "message": "<p>content here</p>",
  "html_url": "https://<canvas>/courses/1/discussion_topics/2",
  "posted_at": "2037-07-21T13:29:31Z",
  "last_reply_at": "2037-07-28T19:38:31Z",
  "require_initial_post": false,
  // Other properties
}
```

## GET
A list of endpoints to fetch discussions from specific courses or groups
>Will respond with a 403 Forbidden status if requires initial post and no one has posted

**List all discussions** 
`/courses/:course_id/discussion_topics`
`/groups/:group_id/discussion_topics`

**Get a single discussion** 
`/courses/:course_id/discussion_topics/:topic_id`
`/groups/:group_id/discussion_topics/:topic_id`

**Get the full topic** 
`courses/:course_id/discussion_topics/:topic_id/view`
`groups/:group_id/discussion_topics/:topic_id/view`

**List topic entries** 
`/courses/:course_id/discussion_topics/:topic_id/entries`
`/groups/:group_id/discussion_topics/:topic_id/entries`

Retrieve the (paginated) top-level entries in a discussion topic.

>If the topic is a root topic with children corresponding to groups of a group assignment, entries from those subtopics for which the user belongs to the corresponding group will be returned.

>Ordering of returned entries is newest-first by posting timestamp (reply activity is ignored).

**List entry replies** 
`courses/:course_id/discussion_topics/:topic_id/entries/:entry_id/replies`
`groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/replies`

**List entries** 
`courses/:course_id/discussion_topics/:topic_id/entry_list`
`groups/:group_id/discussion_topics/:topic_id/entry_list`

## POST

**Create a discussion topic** 
`/courses/:course_id/discussion_topics`
`/groups/:group_id/discussion_topics`

**Reorder pinned topics** 
`/courses/:course_id/discussion_topics/reorder`
`/groups/:group_id/discussion_topics/reorder`

> Requires an order[] parameter containing the order of topics

**Post an entry** 
`/courses/:course_id/discussion_topics/:topic_id/entries`
`/groups/:group_id/discussion_topics/:topic_id/entries`

Create a new entry in a discussion topic.

**Duplicate discussion topic** 
`/courses/:course_id/discussion_topics/:topic_id/duplicate`
`/groups/:group_id/discussion_topics/:topic_id/duplicate`

**Post a reply** 
`/courses/:course_id/discussion_topics/:topic_id/entries/:entry_id/replies`
`/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/replies`

**Rate entry** 
`/courses/:course_id/discussion_topics/:topic_id/entries/:entry_id/rating`
`/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/rating`
>On success, the response will be 204 No Content with an empty body.

# Page
A page object looks like this:
```js
{
  "page_id": 1,
  "url": "my-page-title",
  "title": "My Page Title",
  "created_at": "2012-08-06T16:46:33-06:00",
  "updated_at": "2012-08-08T14:25:20-06:00"
  // Other properties
}
```

## GET

**Show front page** 
`/courses/:course_id/front_page`
`/groups/:group_id/front_page`

**List pages** 
`/courses/:course_id/pages`
`/groups/:group_id/pages`

**Show page** 
`/courses/:course_id/pages/:url_or_id`
`/groups/:group_id/pages/:url_or_id`

**List revisions** 
`/courses/:course_id/pages/:url_or_id/revisions`
`/groups/:group_id/pages/:url_or_id/revisions`

**Show latest revision** 
`/courses/:course_id/pages/:url_or_id/revisions/latest`
`/groups/:group_id/pages/:url_or_id/revisions/latest`

**Show revision** 
`/courses/:course_id/pages/:url_or_id/revisions/:revision_id`
`/groups/:group_id/pages/:url_or_id/revisions/:revision_id`

## POST

**Duplicate page** 
`courses/:course_id/pages/:url_or_id/duplicate`

**Create page** 
`courses/:course_id/pages`
`groups/:group_id/pages`

**Revert to prior version** 
`courses/:course_id/pages/:url_or_id/revisions/:revision_id`
`groups/:group_id/pages/:url_or_id/revisions/:revision_id`

# File
A file object looks like this:
```js
{
  "id": 569,
  "uuid": "SUj23659sdfASF35h265kf352YTdnC4",
  "folder_id": 4207,
  "display_name": "file.txt",
  "filename": "file.txt",
  "content-type": "text/plain",
  "url": "http://www.example.com/files/569",
  // Other properties
}
```

## GET

**Get quota information** 
`courses/:course_id/files/quota`
`groups/:group_id/files/quota`
`users/:user_id/files/quota`

**List files** 
`courses/:course_id/files`
`users/:user_id/files`
`groups/:group_id/files`
`folders/:id/files`

**Get public inline preview URL** 
`files/:id/public_url`

Determine the URL that should be used for inline preview of the file.

**Get file** 
`files/:id`
`courses/:course_id/files/:id`
`groups/:group_id/files/:id`
`users/:user_id/files/:id`

**Translate file reference** 
`courses/:course_id/files/file_ref/:migration_id`

Get information about a file from a course copy file reference

**Get icon metadata** 
`files/:id/icon_metadata`

Returns the icon maker file attachment metadata

## POST

**Create file** 
`files/:id`
`folders/:folder_id/files`

**Reset link verifier** 
`files/:id/reset_verifier`

**Copy a file** 
`folders/:dest_folder_id/copy_file`

# Folder
A Folder object looks like this:
```js
{
  "context_type": "Course",
  "context_id": 1401,
  "files_count": 0,
  "position": 3,
  "updated_at": "2012-07-06T14:58:50Z",
  "folders_url": "https://www.example.com/api/v1/folders/2937/folders",
  "files_url": "https://www.example.com/api/v1/folders/2937/files",
  "full_name": "course files/11folder",
  "lock_at": "2012-07-06T14:58:50Z",
  "id": 2937,
  // Other properties
}
```

## GET

**List nested folders** 
`folders/:id/folders`

**List all folders** 
`courses/:course_id/folders`
`users/:user_id/folders`
`groups/:group_id/folders`

**Resolve path** 
`courses/:course_id/folders/by_path/*full_path`
`courses/:course_id/folders/by_path`

`users/:user_id/folders/by_path/*full_path`
`users/:user_id/folders/by_path`

`groups/:group_id/folders/by_path/*full_path`
`groups/:group_id/folders/by_path`

Given the full path to a folder, returns a list of all Folders in the path hierarchy, starting at the root folder, and ending at the requested folder. 
e.g. `courses/<course_id>/folders/by_path/foo/bar/baz`

>The given path is relative to the context’s root folder and does not include the root folder’s name (e.g., “course files”). If an empty path is given, the context’s root folder alone is returned. Otherwise, if no folder exists with the given full path, a Not Found error is returned.

**Get folder** 
`courses/:course_id/folders/:id`
`users/:user_id/folders/:id`
`groups/:group_id/folders/:id`
`folders/:id`

**Get uploaded media folder for user** 
`courses/:course_id/folders/media`
`groups/:group_id/folders/media`

Returns the details for a designated upload folder that the user has rights to upload to, and creates it if it doesn’t exist.

>If the current user does not have the permissions to manage files in the course or group, the folder will belong to the current user directly.

**List licenses** 
`courses/:course_id/content_licenses`
`groups/:group_id/content_licenses`
`users/:user_id/content_licenses`

Returns a list of license objects:
```js
{
  "id": "cc_by_sa",
  "name": "CC Attribution ShareAlike",
  "url": "http://creativecommons.org/licenses/by-sa/4.0"
}
```

## POST

**Create folder** 
`courses/:course_id/folders`
`users/:user_id/folders`
`groups/:group_id/folders`
`folders/:folder_id/folders`

# Quiz
A quiz object looks like this:
```js
{
  "id": 5,
  "title": "Hamlet Act 3 Quiz",
  "html_url": "http://canvas.example.edu/courses/1/quizzes/2",
  "description": "This is a quiz on Act 3 of Hamlet",
  //'practice_quiz', 'assignment', 'graded_survey'
  "quiz_type": "assignment",
  "assignment_group_id": 3,
  "time_limit": 5
  // Other properties
}
```

## GET

**List quizzes in a course** 
`courses/:course_id/quizzes`

**Get a single quiz** 
`courses/:course_id/quizzes/:id`

## POST

**Create a quiz** 
`courses/:course_id/quizzes`

**Reorder quiz items** 
`courses/:course_id/quizzes/:id/reorder`

**Validate quiz access code** 
`courses/:course_id/quizzes/:id/validate_access_code`
Accepts an access code and returns a Boolean indicating whether that access code is correct

# Module
A module object looks like this:
```js
{
  "id": 123,
  // 'active', 'deleted'
  "workflow_state": "active",
  // (1-based)
  "position": 2,
  "name": "Imaginary Numbers and You",
  "unlock_at": "2012-12-31T06:00:00-06:00",
  "require_sequential_progress": true,
  "prerequisite_module_ids": [121, 122],
  // Other properties
}
```

## GET

**List modules** 
`courses/:course_id/modules`

**Show module** 
`courses/:course_id/modules/:id`

**List module items** 
`courses/:course_id/modules/:module_id/items`

**Show module item** 
`courses/:course_id/modules/:module_id/items/:id`

**Get module item sequence** 
`courses/:course_id/module_item_sequence`

**List a module's overrides** 
`courses/:course_id/modules/:context_module_id/assignment_overrides`

Returns a paginated list of AssignmentOverrides that apply to the ContextModule.

## POST

**Create a module** 
`courses/:course_id/modules`

**Create a module item** 
`courses/:course_id/modules/:module_id/items`

**Select a mastery path** 
`courses/:course_id/modules/:module_id/items/:id/select_mastery_path`

>Requires Mastery Paths feature to be enabled.

**Mark module item read** 
`courses/:course_id/modules/:module_id/items/:id/mark_read`

# SessionlessLaunchUrl
A Sessionless Launch URL is a subset of External Tools. The following is an example of an External Tools object.
```js
{
  "id": 1,
  "domain": "domain.example.com",
  "url": "http://www.example.com/ims/lti",
  "consumer_key": "key",
  "name": "LTI Tool",
  "description": "This is for cool things",
  "created_at": "2037-07-21T13:29:31Z",
  "updated_at": "2037-07-28T19:38:31Z",
  "privacy_level": "anonymous",
  // Other properties
}
```

## GET

**Get a sessionless launch url** 
`courses/:course_id/external_tools/sessionless_launch`
`accounts/:account_id/external_tools/sessionless_launch`
