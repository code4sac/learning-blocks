import { Button } from 'react-bootstrap'
import { FieldApi, useForm } from "@tanstack/react-form"
import { User } from '@/app/utilities/models/user'
import { getRedirectUrl } from '@/utils/utils/urlFunctions'

function FieldInfo({field}: { field: FieldApi<any, any, any, any> }) {
    return <>
        {field.state.meta.touchedErrors ? (
            <em>{field.state.meta.touchedErrors}</em>
        ) : null}
        {field.state.meta.isValidating ? 'Validating...' : null}
    </>
}

export function LoginForm(updateUser, redirectUrl) {
    const form = useForm({
        defaultValues: {
            apiKey: '477abe9e7d27439681d62f4e0de1f5e1',
            schoolCode: '994',
            studentId: '994000001, 994000002',
        },
        onSubmit: async ({value}) => {
            let user = new User()
            user.id = value.studentId[0]
            user.name = value.schoolCode
            //updateUser(user)
            localStorage.setItem('userId', user.id)
            window.location.href = `${window.location.origin}${getRedirectUrl(window.location)}`
        },
    })

    return (
        <div>
            <form.Provider>
                <form
                    onSubmit={(e) => {
                        e.preventDefault()
                        e.stopPropagation()
                        void form.handleSubmit()
                    }}
                >
                    <div>
                        {/*Unable to locate account. Please verify API key. Unable to locate school. Unable to locate one or more of the students. Please verify the Student ID number.*/}
                        <form.Field
                            name='apiKey'
                            validators={{
                                onChange: ({value}) =>
                                    !value
                                        ? 'An API key is required'
                                        : value.length < 16
                                            ? 'API key must be at least 16 characters'
                                            : undefined,
                                onChangeAsyncDebounceMs: 500,
                                onChangeAsync: async ({value}) => {
                                    await new Promise((resolve) => setTimeout(resolve, 1000))
                                    return (
                                        value.includes('error') &&
                                        'No "error" allowed in API key'
                                    )
                                },
                            }}
                            children={(field) => {
                                // Avoid hasty abstractions. Render props are great!
                                return (
                                    <>
                                        <label className={'text-paragraph-p1-semi-bold'} htmlFor={field.name}>API
                                            Key</label>
                                        <br></br>
                                        <input
                                            style={{marginTop: '6px', width: '100%'}}
                                            id={field.name}
                                            name={field.name}
                                            value={field.state.value}
                                            onBlur={field.handleBlur}
                                            onChange={(e) => field.handleChange(e.target.value)}
                                        />
                                        <br></br>
                                        <div className={'login-form-field-info'}>
                                            <FieldInfo field={field}/>
                                        </div>
                                    </>
                                )
                            }}
                        />
                    </div>
                    <div>
                        <form.Field
                            name='schoolCode'
                            children={(field) => (
                                <>
                                    <label className={'loginFormSection text-paragraph-p1-semi-bold'}
                                           htmlFor={field.name}>School Code</label>
                                    <br></br>
                                    <input
                                        style={{marginTop: '6px', width: '100%'}}
                                        id={field.name}
                                        name={field.name}
                                        value={field.state.value}
                                        onBlur={field.handleBlur}
                                        onChange={(e) => field.handleChange(e.target.value)}
                                    />
                                    <div className={'login-form-field-info'}>
                                        <FieldInfo field={field}/>
                                    </div>
                                </>
                            )}
                        />
                    </div>
                    <div>
                        <form.Field
                            name='studentId'
                            children={(field) => (
                                <>
                                    <label className={'loginFormSection text-paragraph-p1-semi-bold'}
                                           htmlFor={field.name}>Student ID</label>
                                    <br></br>
                                    <span className={'text-caption-regular'}>Enter up to 3 Student ID numbers separated by commas</span>
                                    <br></br>
                                    <input
                                        style={{marginTop: '6px', width: '100%'}}
                                        id={field.name}
                                        name={field.name}
                                        value={field.state.value}
                                        onBlur={field.handleBlur}
                                        onChange={(e) => field.handleChange(e.target.value)}
                                    />
                                    <div className={'login-form-field-info'}>
                                        <FieldInfo field={field}/>
                                    </div>
                                </>
                            )}
                        />
                    </div>
                    <form.Subscribe
                        selector={(state) => [state.canSubmit, state.isSubmitting]}
                        children={([canSubmit, isSubmitting]) => (
                            <Button style={{marginTop: '10px'}} className={'loginFormSection'} type='submit'
                                    disabled={!canSubmit}>
                                {isSubmitting ? '...' : 'Submit'}
                            </Button>
                        )}
                    />
                </form>
            </form.Provider>
        </div>
    )
}
