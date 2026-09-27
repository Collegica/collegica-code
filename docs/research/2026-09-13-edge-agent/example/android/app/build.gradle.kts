plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "org.collegica.pocketagent"
    compileSdk = 36
    defaultConfig {
        applicationId = "org.collegica.pocketagent"
        minSdk = 31          // the AI Edge Gallery's floor; Android 12
        targetSdk = 36
        versionCode = 1
        versionName = "0.1"
    }
    buildTypes { release { isMinifyEnabled = false } }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
}

kotlin { compilerOptions { jvmTarget.set(org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_17) } }

dependencies {
    // The whole runtime: engine, conversation, tool calling, GPU delegate.
    implementation("com.google.ai.edge.litertlm:litertlm-android:0.17.0")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.10.2")
}
