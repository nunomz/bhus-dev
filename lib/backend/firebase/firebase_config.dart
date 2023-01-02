import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/foundation.dart';

Future initFirebase() async {
  if (kIsWeb) {
    await Firebase.initializeApp(
        options: FirebaseOptions(
            apiKey: "AIzaSyCfovsKgHXoc5cLJlm3Zqy6ztNr0zyBVA0",
            authDomain: "bhus-520b2.firebaseapp.com",
            projectId: "bhus-520b2",
            storageBucket: "bhus-520b2.appspot.com",
            messagingSenderId: "415296612723",
            appId: "1:415296612723:web:4a4255b7a7509fcea57d06",
            measurementId: "G-5K3MCDR44C"));
  } else {
    await Firebase.initializeApp();
  }
}
